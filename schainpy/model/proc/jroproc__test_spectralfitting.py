class SpectralFitting(Operation):
    '''
        Function GetMoments()

        Input:
        Output:
        Variables modified:
    '''
    isConfig = False
    __dataReady = False
    bloques =  None
    bloque0 = None
    index = 0
    fint = 0
    buffer = 0
    buffer2 = 0
    buffer3 = 0

    def __init__(self):
        Operation.__init__(self)
        self.i=0
        self.isConfig = False
        

    def setup(self,nChan,nProf,nHei,nBlocks):
        self.__dataReady = False
        self.bloques = numpy.zeros([2, nProf, nHei,nBlocks], dtype= complex)
        self.bloque0 = numpy.zeros([nChan, nProf, nHei, nBlocks])

    def __calculateMoments(self,oldspec, oldfreq, n0, nicoh = None, graph = None, smooth = None, type1 = None, fwindow = None, snrth = None, dc = None, aliasing = None, oldfd = None, wwauto = None):
        
        if (nicoh is None): nicoh = 1
        if (graph is None): graph = 0    
        if (smooth is None): smooth = 0
        elif (self.smooth < 3): smooth = 0

        if (type1 is None): type1 = 0
        if (fwindow is None): fwindow = numpy.zeros(oldfreq.size) + 1
        if (snrth is None): snrth = -3
        if (dc is None): dc = 0
        if (aliasing is None): aliasing = 0
        if (oldfd is None): oldfd = 0
        if (wwauto is None): wwauto = 0
         
        if (n0 < 1.e-20):   n0 = 1.e-20
        
        freq = oldfreq
        vec_power = numpy.zeros(oldspec.shape[1])
        vec_fd = numpy.zeros(oldspec.shape[1])
        vec_w = numpy.zeros(oldspec.shape[1])
        vec_snr = numpy.zeros(oldspec.shape[1])
        
        oldspec = numpy.ma.masked_invalid(oldspec)

        for ind in range(oldspec.shape[1]):
                        
            spec = oldspec[:,ind]
            aux = spec*fwindow
            max_spec = aux.max()
            m = list(aux).index(max_spec)
                       
            #Smooth    
            if (smooth == 0):   spec2 = spec
            else:   spec2 = scipy.ndimage.filters.uniform_filter1d(spec,size=smooth)
    
            #    Calculo de Momentos
            bb = spec2[list(range(m,spec2.size))]
            bb = (bb<n0).nonzero()
            bb = bb[0]
            
            ss = spec2[list(range(0,m + 1))]
            ss = (ss<n0).nonzero()
            ss = ss[0]
            
            if (bb.size == 0):
                bb0 = spec.size - 1 - m
            else:   
                bb0 = bb[0] - 1
                if (bb0 < 0):
                    bb0 = 0
                    
            if (ss.size == 0):   ss1 = 1
            else: ss1 = max(ss) + 1
            
            if (ss1 > m):   ss1 = m
            
            valid = numpy.asarray(list(range(int(m + bb0 - ss1 + 1)))) + ss1               
            power = ((spec2[valid] - n0)*fwindow[valid]).sum()
            fd = ((spec2[valid]- n0)*freq[valid]*fwindow[valid]).sum()/power
            w = math.sqrt(((spec2[valid] - n0)*fwindow[valid]*(freq[valid]- fd)**2).sum()/power)
            snr = (spec2.mean()-n0)/n0               
            
            if (snr < 1.e-20) :  
                snr = 1.e-20
            
            vec_power[ind] = power
            vec_fd[ind] = fd
            vec_w[ind] = w
            vec_snr[ind] = snr
        
        moments = numpy.vstack((vec_snr, vec_power, vec_fd, vec_w))
        return moments    

    def __DiffCoherent(self, spectra, cspectra, dataOut, noise, snrth, coh_th, hei_th):

        nProf = dataOut.nProfiles
        heights = dataOut.heightList
        nHei = len(heights)
        channels = dataOut.channelList
        nChan = len(channels)
        crosspairs = dataOut.groupList
        nPairs = len(crosspairs)
        #Separar espectros incoherentes de coherentes snr > 20 dB'
        snr_th = 10**(snrth/10.0)
        my_incoh_spectra = numpy.zeros([nChan, nProf,nHei], dtype='float')
        my_incoh_cspectra = numpy.zeros([nPairs,nProf, nHei], dtype='complex')
        my_incoh_aver = numpy.zeros([nChan, nHei])
        my_coh_aver = numpy.zeros([nChan, nHei])

        coh_spectra = numpy.zeros([nChan, nProf, nHei], dtype='float')
        coh_cspectra = numpy.zeros([nPairs, nProf, nHei], dtype='complex')
        coh_aver = numpy.zeros([nChan, nHei])
 
        incoh_spectra = numpy.zeros([nChan, nProf, nHei], dtype='float')
        incoh_cspectra = numpy.zeros([nPairs, nProf, nHei], dtype='complex')
        incoh_aver = numpy.zeros([nChan, nHei])
        power = numpy.sum(spectra, axis=1)
        
        if coh_th == None : coh_th = numpy.array([0.75,0.65,0.15]) # 0.65
        if hei_th == None : hei_th = numpy.array([60,300,650])
        for ic in range(nPairs):
            pair = crosspairs[ic]
            #si el SNR es mayor que el SNR threshold los datos se toman coherentes
            s_n0 = power[pair[0],:]/noise[pair[0]]
            s_n1 = power[pair[1],:]/noise[pair[1]]
            valid1 =(s_n0>=snr_th).nonzero()
            valid2 = (s_n1>=snr_th).nonzero()
            valid1 =  numpy.array(valid1[0])
            valid2 =  numpy.array(valid2[0])
            valid = valid1
            for iv in range(len(valid2)):
                indv = numpy.array((valid1 == valid2[iv]).nonzero())
                if len(indv[0]) == 0 :
                   valid =  numpy.concatenate((valid,valid2[iv]), axis=None)
            if len(valid)>0:
                my_coh_aver[pair[0],valid]=1	    
                my_coh_aver[pair[1],valid]=1
            # si la coherencia es mayor a la coherencia threshold los datos se toman
            coh = numpy.squeeze(numpy.nansum(cspectra[ic,:,:], axis=0)/numpy.sqrt(numpy.nansum(spectra[pair[0],:,:], axis=0)*numpy.nansum(spectra[pair[1],:,:], axis=0)))
            for ih in range(len(hei_th)):
                hvalid = (heights>hei_th[ih]).nonzero()
                hvalid = hvalid[0]
                if len(hvalid)>0:
                    valid = (numpy.absolute(coh[hvalid])>coh_th[ih]).nonzero()
                    valid = valid[0]
                    if len(valid)>0:
                        my_coh_aver[pair[0],hvalid[valid]] =1
                        my_coh_aver[pair[1],hvalid[valid]] =1
        
            coh_echoes = (my_coh_aver[pair[0],:] == 1).nonzero()
            incoh_echoes = (my_coh_aver[pair[0],:] != 1).nonzero()
            incoh_echoes = incoh_echoes[0]
            if len(incoh_echoes) > 0:
                my_incoh_spectra[pair[0],:,incoh_echoes] = spectra[pair[0],:,incoh_echoes]
                my_incoh_spectra[pair[1],:,incoh_echoes] = spectra[pair[1],:,incoh_echoes]
                my_incoh_cspectra[ic,:,incoh_echoes] = cspectra[ic,:,incoh_echoes]
                my_incoh_aver[pair[0],incoh_echoes] = 1
                my_incoh_aver[pair[1],incoh_echoes] = 1

        
        for ic in range(nPairs):
            pair = crosspairs[ic]

            valid1 =(my_coh_aver[pair[0],:]==1 ).nonzero()
            valid2 = (my_coh_aver[pair[1],:]==1).nonzero()
            valid1 = numpy.array(valid1[0])
            valid2 = numpy.array(valid2[0])
            valid = valid1

            for iv in range(len(valid2)):

                indv = numpy.array((valid1 == valid2[iv]).nonzero())
                if len(indv[0]) == 0 :
                   valid =  numpy.concatenate((valid,valid2[iv]), axis=None)
            valid1 =(my_coh_aver[pair[0],:] !=1 ).nonzero()
            valid2 = (my_coh_aver[pair[1],:] !=1).nonzero()
            valid1 = numpy.array(valid1[0])
            valid2 = numpy.array(valid2[0])
            incoh_echoes = valid1
            for iv in range(len(valid2)):

                indv = numpy.array((valid1 == valid2[iv]).nonzero())
                if len(indv[0]) == 0 :
                   incoh_echoes = numpy.concatenate(( incoh_echoes,valid2[iv]), axis=None)

            if len(valid)>0:
                coh_spectra[pair[0],:,valid] = spectra[pair[0],:,valid]
                coh_spectra[pair[1],:,valid] = spectra[pair[1],:,valid]
                coh_cspectra[ic,:,valid] = cspectra[ic,:,valid]
                coh_aver[pair[0],valid]=1
                coh_aver[pair[1],valid]=1
            if len(incoh_echoes)>0:
                incoh_spectra[pair[0],:,incoh_echoes] = spectra[pair[0],:,incoh_echoes]
                incoh_spectra[pair[1],:,incoh_echoes] = spectra[pair[1],:,incoh_echoes]
                incoh_cspectra[ic,:,incoh_echoes] = cspectra[ic,:,incoh_echoes]
                incoh_aver[pair[0],incoh_echoes]=1
                incoh_aver[pair[1],incoh_echoes]=1
        return  my_incoh_spectra ,my_incoh_cspectra,my_incoh_aver,my_coh_aver, incoh_spectra, coh_spectra, incoh_cspectra, coh_cspectra, incoh_aver, coh_aver


    def __CleanCoherent(self,snrth, spectra, cspectra, coh_aver,dataOut, noise,clean_coh_echoes,index):

        nProf = dataOut.nProfiles
        heights = dataOut.heightList
        nHei = len(heights)
        channels = dataOut.channelList
        nChan = len(channels)
        crosspairs = dataOut.groupList
        nPairs = len(crosspairs)
        
        absc = dataOut.abscissaList[:-1]
        data_param = numpy.zeros((nChan, 4, spectra.shape[2]))
        clean_coh_spectra = spectra.copy()
        clean_coh_cspectra = cspectra.copy()
        clean_coh_aver = coh_aver.copy()

        spwd_th=[10,6]  #spwd_th[0] --> For satellites ; spwd_th[1] --> For special events like SUN.
        coh_th = 0.75

        rtime0 = [6,18] # periodo sin ESF
        rtime1 = [10.5,13.5] # periodo con alta coherencia y alto ancho espectral (esperado): SOL.

        time = index*5./60 # en base a 5 min de proceso
        if clean_coh_echoes == 1 :
           for ind in range(nChan):
              data_param[ind,:,:] = self.__calculateMoments( spectra[ind,:,:] , absc , noise[ind] )
           spwd = data_param[:,3]
        #  SPECB_JULIA,header=anal_header,jspectra=spectra,vel=velocities,hei=heights, num_aver=1, mode_fit=0,smoothing=smoothing,jvelr=velr,jspwd=spwd,jsnr=snr,jnoise=noise,jstdvnoise=stdvnoise
      # para obtener spwd
           for ic in range(nPairs):
              pair = crosspairs[ic]
              coh = numpy.squeeze(numpy.sum(cspectra[ic,:,:], axis=1)/numpy.sqrt(numpy.sum(spectra[pair[0],:,:], axis=1)*numpy.sum(spectra[pair[1],:,:], axis=1)))
              for ih in range(nHei) :
        # Considering heights higher than 200km in order to avoid removing phenomena like EEJ.
                 if heights[ih] >= 200 and coh_aver[pair[0],ih] == 1 and coh_aver[pair[1],ih] == 1 :
          # Checking coherence
                    if (numpy.abs(coh[ih]) <= coh_th) or (time >= rtime0[0] and time <= rtime0[1]) :
            # Checking spectral widths
                       if (spwd[pair[0],ih] > spwd_th[0]) or (spwd[pair[1],ih] > spwd_th[0]) :
              # satelite
                          clean_coh_spectra[pair,ih,:] = 0.0
                          clean_coh_cspectra[ic,ih,:] =  0.0
                          clean_coh_aver[pair,ih] = 0
                       else :
                            if ((spwd[pair[0],ih] < spwd_th[1]) or (spwd[pair[1],ih] < spwd_th[1])) :
                # Especial event like sun.
                               clean_coh_spectra[pair,ih,:] = 0.0
                               clean_coh_cspectra[ic,ih,:] =  0.0
                               clean_coh_aver[pair,ih] = 0

        return clean_coh_spectra, clean_coh_cspectra, clean_coh_aver

    def CleanRayleigh(self,dataOut,spectra,cspectra,save_drifts):

        rfunc = cspectra.copy()
        n_funct = len(rfunc[0,:,0,0])
        val_spc = spectra*0.0 
        val_cspc = cspectra*0.0
        in_sat_spectra = spectra.copy()  
        in_sat_cspectra = cspectra.copy()

        min_hei = 200
        nProf = dataOut.nProfiles
        heights = dataOut.heightList
        nHei = len(heights)
        channels = dataOut.channelList
        nChan = len(channels)
        crosspairs = dataOut.groupList
        nPairs = len(crosspairs)
        hval=(heights >= min_hei).nonzero()
        ih=hval[0]
        for ih in range(hval[0][0],nHei):
            for ifreq in range(nProf):
                for ii in range(n_funct):
                    
                    func2clean = 10*numpy.log10(numpy.absolute(rfunc[:,ii,ifreq,ih]))
                    val = (numpy.isfinite(func2clean)==True).nonzero()
                    if len(val)>0:                   
                       min_val = numpy.around(numpy.amin(func2clean)-2) #> (-40)
                       if min_val <= -40 : min_val = -40
                       max_val = numpy.around(numpy.amax(func2clean)+2) #< 200
                       if max_val >= 200 : max_val = 200
                       step = 1
                       #Getting bins and the histogram
                       x_dist = min_val + numpy.arange(1 + ((max_val-(min_val))/step))*step
                       y_dist,binstep = numpy.histogram(func2clean,bins=range(int(min_val),int(max_val+2),step))                                                
                       mean = numpy.sum(x_dist * y_dist) / numpy.sum(y_dist)
                       sigma = numpy.sqrt(numpy.sum(y_dist * (x_dist - mean)**2) / numpy.sum(y_dist))
                       parg = [numpy.amax(y_dist),mean,sigma]
                       try :
                           gauss_fit, covariance = curve_fit(fit_func, x_dist, y_dist,p0=parg)
                           mode = gauss_fit[1]
                           stdv = gauss_fit[2] 
                       except:
                           mode = mean
                           stdv = sigma 

                       #Removing echoes greater than mode + 3*stdv
                       factor_stdv = 2.5
                       noval = (abs(func2clean - mode)>=(factor_stdv*stdv)).nonzero()
                       
                       if len(noval[0]) > 0:
                            novall = ((func2clean - mode) >= (factor_stdv*stdv)).nonzero()
                            cross_pairs = crosspairs[ii]
                                #Getting coherent echoes which are removed.
                            if len(novall[0]) > 0:
                                val_spc[novall[0],cross_pairs[0],ifreq,ih] = 1
                                val_spc[novall[0],cross_pairs[1],ifreq,ih] = 1
                                val_cspc[novall[0],ii,ifreq,ih] = 1
                                #Removing coherent from ISR data
                            spectra[noval,cross_pairs[0],ifreq,ih] = numpy.nan
                            spectra[noval,cross_pairs[1],ifreq,ih] = numpy.nan
                            cspectra[noval,ii,ifreq,ih] = numpy.nan

            #Getting average of the spectra and cross-spectra from incoherent echoes.
        out_spectra = numpy.zeros([nChan,nProf,nHei], dtype=float) #+numpy.nan
        out_cspectra = numpy.zeros([nPairs,nProf,nHei], dtype=complex) #+numpy.nan
        for ih in range(nHei):
            for ifreq in range(nProf):
                for ich in range(nChan):                    
                    tmp = spectra[:,ich,ifreq,ih] 
                    valid = (numpy.isfinite(tmp[:])==True).nonzero() 
                    if len(valid[0]) >0 :
                       out_spectra[ich,ifreq,ih] = numpy.nansum(tmp)/len(valid[0])
                for icr in range(nPairs):
                    tmp = numpy.squeeze(cspectra[:,icr,ifreq,ih])
                    valid = (numpy.isfinite(tmp)==True).nonzero()
                    if len(valid[0]) > 0:
                        out_cspectra[icr,ifreq,ih] = numpy.nansum(tmp)/len(valid[0])
            #Removing fake coherent echoes (at least 4 points around the point)
        val_spectra = numpy.sum(val_spc,0)
        val_cspectra = numpy.sum(val_cspc,0)
        
        val_spectra = self.REM_ISOLATED_POINTS(val_spectra,4)
        val_cspectra = self.REM_ISOLATED_POINTS(val_cspectra,4)
        
        for i in range(nChan):
            for j in range(nProf):
                for k in range(nHei):
                    if numpy.isfinite(val_spectra[i,j,k]) and val_spectra[i,j,k] < 1 :
                        val_spc[:,i,j,k] = 0.0
        for i in range(nPairs):
            for j in range(nProf):
                for k in range(nHei):
                    if numpy.isfinite(val_cspectra[i,j,k]) and val_cspectra[i,j,k] < 1 :
                        val_cspc[:,i,j,k] = 0.0

        tmp_sat_spectra = spectra.copy()
        tmp_sat_spectra = tmp_sat_spectra*numpy.nan
        tmp_sat_cspectra = cspectra.copy()
        tmp_sat_cspectra = tmp_sat_cspectra*numpy.nan
        val = (val_spc > 0).nonzero()
        if len(val[0]) > 0:              
                tmp_sat_spectra[val] = in_sat_spectra[val]
            
        val = (val_cspc > 0).nonzero()
        if len(val[0]) > 0:
                tmp_sat_cspectra[val] = in_sat_cspectra[val]

            #Getting average of the spectra and cross-spectra from incoherent echoes.
        sat_spectra = numpy.zeros((nChan,nProf,nHei), dtype=float)
        sat_cspectra = numpy.zeros((nPairs,nProf,nHei), dtype=complex)
        for ih in range(nHei):
            for ifreq in range(nProf):
                for ich in range(nChan):
                    tmp = numpy.squeeze(tmp_sat_spectra[:,ich,ifreq,ih])
                    valid = (numpy.isfinite(tmp)).nonzero()                    
                    if len(valid[0]) > 0:
                        sat_spectra[ich,ifreq,ih] = numpy.nansum(tmp)/len(valid[0])

                for icr in range(nPairs):
                    tmp = numpy.squeeze(tmp_sat_cspectra[:,icr,ifreq,ih])
                    valid = (numpy.isfinite(tmp)).nonzero()
                    if len(valid[0]) > 0:
                        sat_cspectra[icr,ifreq,ih] = numpy.nansum(tmp)/len(valid[0])
        return out_spectra, out_cspectra,sat_spectra,sat_cspectra
    def REM_ISOLATED_POINTS(self,array,rth):
        if rth == None : rth = 4
        num_prof = len(array[0,:,0])
        num_hei = len(array[0,0,:])
        n2d = len(array[:,0,0])
 
        for ii in range(n2d) :
          tmp = array[ii,:,:]
          tmp = numpy.reshape(tmp,num_prof*num_hei)
          indxs1 = (numpy.isfinite(tmp)==True).nonzero()
          indxs2 = (tmp > 0).nonzero() 
          indxs1 = (indxs1[0])
          indxs2 = indxs2[0]
          indxs = None
          for iv in range(len(indxs2)):
                indv = numpy.array((indxs1 == indxs2[iv]).nonzero())
                if len(indv[0]) > 0  :
                   indxs =  numpy.concatenate((indxs,indxs2[iv]), axis=None)
          indxs = indxs[1:]
          if len(indxs) < 4 :
            array[ii,:,:] = 0.
            return
          
          xpos = numpy.mod(indxs ,num_hei)
          ypos = (indxs / num_hei)
          sx = numpy.argsort(xpos) # Ordering respect to "x" (time)
          xpos = xpos[sx]
          ypos = ypos[sx]
        # *********************************** Cleaning isolated points **********************************
          ic = 0
          while True : 
            r = numpy.sqrt(list(numpy.power((xpos[ic]-xpos),2)+ numpy.power((ypos[ic]-ypos),2)))
            no_coh1 = (numpy.isfinite(r)==True).nonzero()
            no_coh2 = (r <= rth).nonzero()
            no_coh1 = numpy.array(no_coh1[0])
            no_coh2 = numpy.array(no_coh2[0])
            no_coh = None
            for iv in range(len(no_coh2)):
                indv = numpy.array((no_coh1 == no_coh2[iv]).nonzero())
                if len(indv[0]) > 0  :
                   no_coh =  numpy.concatenate((no_coh,no_coh2[iv]), axis=None)
            no_coh = no_coh[1:]
            if len(no_coh) < 4 :
               xpos[ic] = numpy.nan
               ypos[ic] = numpy.nan
            
            ic = ic + 1      
            if  (ic == len(indxs)) : 
                break
          indxs = (numpy.isfinite(list(xpos))==True).nonzero()
          if len(indxs[0]) < 4 :
             array[ii,:,:] = 0.
             return
    
          xpos = xpos[indxs[0]]
          ypos = ypos[indxs[0]]
          for i in range(0,len(ypos)):
    	      ypos[i]=int(ypos[i])
          junk = tmp
          tmp = junk*0.0
          
          tmp[list(xpos + (ypos*num_hei))] = junk[list(xpos + (ypos*num_hei))] 
          array[ii,:,:] = numpy.reshape(tmp,(num_prof,num_hei))
        return array

    def moments(self,doppler,yarray,npoints):
        ytemp = yarray
        val = (ytemp > 0).nonzero()
        val = val[0]
        if len(val) == 0 : val = range(npoints-1) 
        
        ynew = 0.5*(ytemp[val[0]]+ytemp[val[len(val)-1]])
        ytemp[len(ytemp):] = [ynew]

        index = 0
        index = numpy.argmax(ytemp)
        ytemp = numpy.roll(ytemp,int(npoints/2)-1-index)
        ytemp = ytemp[0:npoints-1]

        fmom = numpy.sum(doppler*ytemp)/numpy.sum(ytemp)+(index-(npoints/2-1))*numpy.abs(doppler[1]-doppler[0])
        smom = numpy.sum(doppler*doppler*ytemp)/numpy.sum(ytemp)
        return [fmom,numpy.sqrt(smom)]





    def run(self, dataOut, getSNR = True, path=None, file=None, groupList=None, filec=None,coh_th=None, hei_th=None,taver=None,proc=None,nhei=None,nprofs=None,ipp=None,channelList=None):
        if not numpy.any(proc):
            nChannels = dataOut.nChannels
            nHeights= dataOut.heightList.size
            nProf = dataOut.nProfiles
            if numpy.any(taver): taver=int(taver)
            else : taver = 5
            tini=time.localtime(dataOut.utctime)
            if (tini.tm_min % taver) == 0 and (tini.tm_sec < 5 and self.fint==0):
                self.index = 0
                jspc = self.buffer
                jcspc = self.buffer2
                jnoise = self.buffer3
                self.buffer = dataOut.data_spc
                self.buffer2 = dataOut.data_cspc
                self.buffer3 = dataOut.noise
                self.fint = 1
                if numpy.any(jspc) :
                    jspc= numpy.reshape(jspc,(int(len(jspc)/nChannels),nChannels,nProf,nHeights))
                    jcspc= numpy.reshape(jcspc,(int(len(jcspc)/int(nChannels/2)),int(nChannels/2),nProf,nHeights))
                    jnoise= numpy.reshape(jnoise,(int(len(jnoise)/nChannels),nChannels))
                else:
                    dataOut.flagNoData = True
                    return dataOut
            else :
                if (tini.tm_min % taver) == 0 : self.fint = 1
                else : self.fint = 0
                self.index += 1
                if numpy.any(self.buffer):
                    self.buffer = numpy.concatenate((self.buffer,dataOut.data_spc), axis=0)
                    self.buffer2 = numpy.concatenate((self.buffer2,dataOut.data_cspc), axis=0)
                    self.buffer3 = numpy.concatenate((self.buffer3,dataOut.noise), axis=0)
                else:
                    self.buffer = dataOut.data_spc
                    self.buffer2 = dataOut.data_cspc
                    self.buffer3 = dataOut.noise
                dataOut.flagNoData = True
                return dataOut
            if path != None:
                sys.path.append(path)
            self.library = importlib.import_module(file)
            if filec != None:
                self.weightf = importlib.import_module(filec)

            #To be inserted as a parameter
            groupArray = numpy.array(groupList)
            #groupArray = numpy.array([[0,1],[2,3]]) 
            dataOut.groupList = groupArray
            nGroups = groupArray.shape[0]
            nChannels = dataOut.nChannels
            nHeights = dataOut.heightList.size

            #Parameters Array
            dataOut.data_param = None
            dataOut.data_paramC = None
            dataOut.clean_num_aver = None
            dataOut.coh_num_aver = None
            dataOut.tmp_spectra_i = None
            dataOut.tmp_cspectra_i = None
            dataOut.tmp_spectra_c = None
            dataOut.tmp_cspectra_c = None
            dataOut.index = None

            #Set constants
            constants = self.library.setConstants(dataOut)
            dataOut.constants = constants
            M = dataOut.normFactor
            N = dataOut.nFFTPoints
            ippSeconds = dataOut.ippSeconds
            K = dataOut.nIncohInt
            pairsArray = numpy.array(dataOut.pairsList)
            snrth= 20
            spectra = dataOut.data_spc
            cspectra = dataOut.data_cspc
            nProf = dataOut.nProfiles
            heights = dataOut.heightList
            nHei = len(heights)
            channels = dataOut.channelList
            nChan = len(channels)
            nIncohInt = dataOut.nIncohInt
            crosspairs = dataOut.groupList
            noise = dataOut.noise
            jnoise = jnoise/N
            noise = numpy.nansum(jnoise,axis=0)#/len(jnoise)
            power = numpy.sum(spectra, axis=1)
            nPairs = len(crosspairs)
            absc = dataOut.abscissaList[:-1]

            if not self.isConfig:
                self.isConfig = True

            index = tini.tm_hour*12+tini.tm_min/taver
            dataOut.index= index
            jspc = jspc/N/N
            jcspc = jcspc/N/N
            tmp_spectra,tmp_cspectra,sat_spectra,sat_cspectra = self.CleanRayleigh(dataOut,jspc,jcspc,2)
            jspectra = tmp_spectra*len(jspc[:,0,0,0])
            jcspectra = tmp_cspectra*len(jspc[:,0,0,0])
            my_incoh_spectra ,my_incoh_cspectra,my_incoh_aver,my_coh_aver, incoh_spectra, coh_spectra, incoh_cspectra, coh_cspectra, incoh_aver, coh_aver = self.__DiffCoherent(jspectra, jcspectra, dataOut, noise, snrth,coh_th, hei_th)
            clean_coh_spectra, clean_coh_cspectra, clean_coh_aver = self.__CleanCoherent(snrth, coh_spectra, coh_cspectra, coh_aver, dataOut, noise,1,index)                                        
            dataOut.data_spc = incoh_spectra
            dataOut.data_cspc = incoh_cspectra
            clean_num_aver = incoh_aver*len(jspc[:,0,0,0])
            coh_num_aver = clean_coh_aver*len(jspc[:,0,0,0])
            dataOut.clean_num_aver = clean_num_aver
            dataOut.coh_num_aver = coh_num_aver
            dataOut.tmp_spectra_i = incoh_spectra
            dataOut.tmp_cspectra_i = incoh_cspectra
            dataOut.tmp_spectra_c = clean_coh_spectra
            dataOut.tmp_cspectra_c = clean_coh_cspectra
            #List of possible combinations
            listComb = itertools.combinations(numpy.arange(groupArray.shape[1]),2)
            indCross = numpy.zeros(len(list(listComb)), dtype = 'int')
            if getSNR:
                listChannels = groupArray.reshape((groupArray.size))
                listChannels.sort()
                dataOut.data_SNR = self.__getSNR(dataOut.data_spc[listChannels,:,:], noise[listChannels])
        else:
            clean_num_aver = dataOut.clean_num_aver
            coh_num_aver = dataOut.coh_num_aver
            dataOut.data_spc = dataOut.tmp_spectra_i
            dataOut.data_cspc = dataOut.tmp_cspectra_i
            clean_coh_spectra = dataOut.tmp_spectra_c
            clean_coh_cspectra = dataOut.tmp_cspectra_c
            jspectra = dataOut.data_spc+clean_coh_spectra
            nHeights = len(dataOut.heightList) # nhei
            nProf = int(dataOut.nProfiles)
            dataOut.nProfiles = nProf
            dataOut.data_param = None
            dataOut.data_paramC = None
            dataOut.code = numpy.array([[-1.,-1.,1.],[1.,1.,-1.]])
            #M=600
            #N=200
            dataOut.flagDecodeData=True
            M = int(dataOut.normFactor)
            N = int(dataOut.nFFTPoints)
            dataOut.nFFTPoints = N
            dataOut.nIncohInt= int(dataOut.nIncohInt)
            dataOut.nProfiles = int(dataOut.nProfiles)
            dataOut.nCohInt = int(dataOut.nCohInt)
            print('sale',dataOut.nProfiles,dataOut.nHeights)
            #dataOut.nFFTPoints=nprofs
            #dataOut.normFactor = nprofs
            dataOut.channelList = channelList
            #dataOut.ippFactor=1
            #ipp = ipp/150*1.e-3
            vmax = (300000000/49920000.0/2) / (dataOut.ippSeconds)
            #dataOut.ippSeconds=ipp
            absc = vmax*( numpy.arange(nProf,dtype='float')-nProf/2.)/nProf
            print('sale 2',dataOut.ippSeconds,M,N)
            print('Empieza procesamiento offline')
            if path != None:
                sys.path.append(path)
            self.library = importlib.import_module(file)
            constants = self.library.setConstants(dataOut)
            constants['M'] = M
            dataOut.constants = constants
        
        groupArray = numpy.array(groupList)
        dataOut.groupList = groupArray
        nGroups = groupArray.shape[0]
        #List of possible combinations
        listComb = itertools.combinations(numpy.arange(groupArray.shape[1]),2)
        indCross = numpy.zeros(len(list(listComb)), dtype = 'int')
        if dataOut.data_paramC is None:
                    dataOut.data_paramC = numpy.zeros((nGroups*4, nHeights,2))*numpy.nan 
        for i in range(nGroups): 
            coord = groupArray[i,:]
            #Input data array
            data = dataOut.data_spc[coord,:,:]/(M*N)
            data = data.reshape((data.shape[0]*data.shape[1],data.shape[2]))

            #Cross Spectra data array for Covariance Matrixes
            ind = 0
            for pairs in listComb:
                pairsSel = numpy.array([coord[x],coord[y]])
                indCross[ind] = int(numpy.where(numpy.all(pairsArray == pairsSel, axis = 1))[0][0])
                ind += 1
            dataCross = dataOut.data_cspc[indCross,:,:]/(M*N)
            dataCross = dataCross**2
            nhei = nHeights
            poweri = numpy.sum(dataOut.data_spc[:,1:nProf-0,:],axis=1)/clean_num_aver[:,:]
            if i == 0 : my_noises = numpy.zeros(4,dtype=float)
            n0i = numpy.nanmin(poweri[0+i*2,0:nhei-0])/(nProf-1)
            n1i = numpy.nanmin(poweri[1+i*2,0:nhei-0])/(nProf-1)
            n0 = n0i
            n1=  n1i
            my_noises[2*i+0] = n0
            my_noises[2*i+1] = n1
            snrth = -15.0 # -4 -16 -25
            snrth = 10**(snrth/10.0)
            jvelr = numpy.zeros(nHeights, dtype = 'float')
            hvalid = [0]
            coh2 = abs(dataOut.data_cspc[i,1:nProf,:])**2/(dataOut.data_spc[0+i*2,1:nProf-0,:]*dataOut.data_spc[1+i*2,1:nProf-0,:])
            for h in range(nHeights):
                smooth = clean_num_aver[i+1,h]
                signalpn0 = (dataOut.data_spc[i*2,1:(nProf-0),h])/smooth
                signalpn1 = (dataOut.data_spc[i*2+1,1:(nProf-0),h])/smooth
                signal0 = signalpn0-n0
                signal1 = signalpn1-n1
                snr0 = numpy.sum(signal0/n0)/(nProf-1)
                snr1 = numpy.sum(signal1/n1)/(nProf-1)
                gamma = coh2[:,h]
                indxs = (numpy.isfinite(list(gamma))==True).nonzero()
                if len(indxs) >0:
                   if numpy.nanmean(gamma) > 0.07:
                      maxp0 = numpy.argmax(signal0*gamma)
                      maxp1 = numpy.argmax(signal1*gamma)
                      #print('usa gamma',numpy.nanmean(gamma))
                   else:
                      maxp0 = numpy.argmax(signal0)
                      maxp1 = numpy.argmax(signal1)
                   jvelr[h] = (absc[maxp0]+absc[maxp1])/2.
                else: jvelr[h] = absc[0]
                if snr0 > 0.1 and snr1 > 0.1: hvalid = numpy.concatenate((hvalid,h), axis=None)
                #print(maxp0,absc[maxp0],snr0,jvelr[h])
            
            if len(hvalid)> 1: fd0 = numpy.median(jvelr[hvalid[1:]])*-1
            else: fd0 = numpy.nan 
            for h in range(nHeights):
                d = data[:,h]
                smooth = clean_num_aver[i+1,h] #dataOut.data_spc[:,1:nProf-0,:]
                signalpn0 = (dataOut.data_spc[i*2,1:(nProf-0),h])/smooth
                signalpn1 = (dataOut.data_spc[i*2+1,1:(nProf-0),h])/smooth
                signal0 = signalpn0-n0
                signal1 = signalpn1-n1
                snr0 = numpy.sum(signal0/n0)/(nProf-1)
                snr1 = numpy.sum(signal1/n1)/(nProf-1)
                if snr0 > snrth and snr1 > snrth and clean_num_aver[i+1,h] > 0 :
                #Covariance Matrix
                    D = numpy.diag(d**2)
                    ind = 0
                    for pairs in listComb:
                    #Coordinates in Covariance Matrix
                        x = pairs[0]    
                        y = pairs[1]
                    #Channel Index
                        S12 = dataCross[ind,:,h]
                        D12 = numpy.diag(S12)
                    #Completing Covariance Matrix with Cross Spectras
                        D[x*N:(x+1)*N,y*N:(y+1)*N] = D12
                        D[y*N:(y+1)*N,x*N:(x+1)*N] = D12
                        ind += 1
                    diagD = numpy.zeros(256)

                    try:
                       Dinv=numpy.linalg.inv(D)
                       L=numpy.linalg.cholesky(Dinv)
                    except:
                       Dinv = D*numpy.nan
                       L= D*numpy.nan
                    LT=L.T

                    dp = numpy.dot(LT,d)
                #Initial values
                    data_spc = dataOut.data_spc[coord,:,h]
                    w = data_spc/data_spc
                    if filec != None:
                       w = self.weightf.weightfit(w,tini.tm_year,tini.tm_yday,index,h,i)
                    if (h>6)and(error1[3]<25):
                        p0 = dataOut.data_param[i,:,h-1]
                    else:
                        p0 = numpy.array(self.library.initialValuesFunction(data_spc*w, constants))# sin el i(data_spc, constants, i)
                    p0[3] = fd0
                    if filec != None:
                       p0 = self.weightf.Vrfit(p0,tini.tm_year,tini.tm_yday,index,h,i)
                    try:
                    #Least Squares
                        minp,covp,infodict,mesg,ier = optimize.leastsq(self.__residFunction,p0,args=(dp,LT,constants),full_output=True)
                    #minp,covp = optimize.leastsq(self.__residFunction,p0,args=(dp,LT,constants))
                    #Chi square error
                        error0 = numpy.sum(infodict['fvec']**2)/(2*N)
                    #Error with Jacobian
                        error1 = self.library.errorFunction(minp,constants,LT)

                    except:
                        minp = p0*numpy.nan
                        error0 = numpy.nan
                        error1 = p0*numpy.nan
                else :
                    data_spc = dataOut.data_spc[coord,:,h]
                    p0 = numpy.array(self.library.initialValuesFunction(data_spc, constants))
                    minp = p0*numpy.nan
                    error0 = numpy.nan
                    error1 = p0*numpy.nan                                       
                if dataOut.data_param is None:
                    dataOut.data_param = numpy.zeros((nGroups, p0.size, nHeights))*numpy.nan
                    dataOut.data_error = numpy.zeros((nGroups, p0.size + 1, nHeights))*numpy.nan
                
                dataOut.data_error[i,:,h] = numpy.hstack((error0,error1))
                dataOut.data_param[i,:,h] = minp
            for ht in range(nHeights-1) :
                smooth = coh_num_aver[i+1,ht] #datc[0,ht,0,beam] 
                dataOut.data_paramC[4*i,ht,1] = smooth
                signalpn0 = (clean_coh_spectra[i*2  ,1:(nProf-0),ht])/smooth #coh_spectra
                signalpn1 = (clean_coh_spectra[i*2+1,1:(nProf-0),ht])/smooth   
                val0 = (signalpn0 > 0).nonzero()
                val0 = val0[0]
                if len(val0) == 0 : val0_npoints = nProf 
                else : val0_npoints = len(val0) 
                
                val1 = (signalpn1 > 0).nonzero()
                val1 = val1[0]
                if len(val1) == 0 : val1_npoints = nProf
                else : val1_npoints = len(val1)

                dataOut.data_paramC[0+4*i,ht,0] = numpy.sum((signalpn0/val0_npoints))/n0
                dataOut.data_paramC[1+4*i,ht,0] = numpy.sum((signalpn1/val1_npoints))/n1
        
                signal0 = (signalpn0-n0) 
                vali = (signal0 < 0).nonzero()
                vali = vali[0]
                if len(vali) > 0 : signal0[vali] = 0
                signal1 = (signalpn1-n1) 
                vali = (signal1 < 0).nonzero()
                vali = vali[0]
                if len(vali) > 0 : signal1[vali] = 0
                snr0 = numpy.sum(signal0/n0)/(nProf-1)
                snr1 = numpy.sum(signal1/n1)/(nProf-1)
                doppler = absc[1:]
                if snr0 >= snrth and snr1 >= snrth and smooth :
                    signalpn0_n0 = signalpn0
                    signalpn0_n0[val0] = signalpn0[val0] - n0
                    mom0 = self.moments(doppler,signalpn0-n0,nProf)
                    signalpn1_n1 = signalpn1
                    signalpn1_n1[val1] = signalpn1[val1] - n1
                    mom1 = self.moments(doppler,signalpn1_n1,nProf)
                    dataOut.data_paramC[2+4*i,ht,0] = (mom0[0]+mom1[0])/2.
                    dataOut.data_paramC[3+4*i,ht,0] = (mom0[1]+mom1[1])/2.

        dataOut.data_spc = jspectra
        dataOut.spc_noise = my_noises*nProf*M
        if numpy.any(proc): dataOut.spc_noise = my_noises*nProf*M
        if getSNR:
            listChannels = groupArray.reshape((groupArray.size))
            listChannels.sort()

            dataOut.data_snr = self.__getSNR(dataOut.data_spc[listChannels,:,:], my_noises[listChannels])
        return dataOut
    
    def __residFunction(self, p, dp, LT, constants):

        fm = self.library.modelFunction(p, constants)
        fmp=numpy.dot(LT,fm)
        return  dp-fmp

    def __getSNR(self, z, noise):

        avg = numpy.average(z, axis=1)
        SNR = (avg.T-noise)/noise
        SNR = SNR.T
        return SNR

    def __chisq(self, p, chindex, hindex):
        #similar to Resid but calculates CHI**2
        [LT,d,fm]=setupLTdfm(p,chindex,hindex)
        dp=numpy.dot(LT,d)
        fmp=numpy.dot(LT,fm)
        chisq=numpy.dot((dp-fmp).T,(dp-fmp))
        return chisq
