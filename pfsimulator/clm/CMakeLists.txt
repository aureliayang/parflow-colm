
set (SRC_FILES
  ${CMAKE_CURRENT_BINARY_DIR}/parflow_config.F90
  ./mkinidata/CoLMINI.F90
  ./mkinidata/MOD_Initialize.F90
  ./mkinidata/MOD_IniTimeVariable.F90
  ./mkinidata/MOD_SoilColorRefl.F90
  ./mkinidata/MOD_HtopReadin.F90
  ./mkinidata/MOD_LakeDepthReadin.F90
  ./share/MOD_Precision.F90                           
  ./share/MOD_SPMD_Task.F90                           
  ./share/MOD_Namelist.F90
  ./share/MOD_Utils.F90                               
  ./share/MOD_UserDefFun.F90                          
  ./share/MOD_TimeManager.F90 
  ./HYDRO/MOD_Hydro_SoilFunction.F90                                             
  MOD_Vars_Global.F90                         
  MOD_Const_Physical.F90                      
  MOD_Const_LC.F90                                                    
  MOD_Const_PFT.F90                           
  MOD_Vars_TimeInvariants.F90                 
  MOD_Vars_TimeVariables.F90                  
  MOD_Vars_1DFluxes.F90                       
  MOD_Vars_1DForcing.F90                                           
  MOD_Eroot.F90                               
  MOD_Qsadv.F90                               
  MOD_LAIEmpirical.F90                        
  MOD_NitrifData.F90                          
  MOD_NdepData.F90                            
  MOD_FireData.F90                            
  MOD_OrbCoszen.F90                           
  MOD_OrbCosazi.F90                           
  MOD_3DCanopyRadiation.F90                   
  MOD_Aerosol.F90                             
  MOD_SnowSnicar.F90                          
  MOD_Albedo.F90                              
  MOD_SnowFraction.F90                        
  MOD_MonthlyinSituCO2MaunaLoa.F90                                                     
  MOD_Irrigation.F90                          
  MOD_AssimStomataConductance.F90             
  MOD_PlantHydraulic.F90                      
  MOD_FrictionVelocity.F90                    
  MOD_TurbulenceLEddy.F90                     
  MOD_Ozone.F90                               
  MOD_CanopyLayerProfile.F90                  
  MOD_LeafTemperature.F90                     
  MOD_LeafTemperaturePC.F90                   
  MOD_SoilThermalParameters.F90               
  MOD_SoilSnowHydrology.F90                   
  MOD_SnowLayersCombineDivide.F90             
  MOD_PhaseChange.F90
  MOD_Glacier.F90                                                     
  MOD_Lake.F90                                
  MOD_SimpleOcean.F90                         
  MOD_GroundFluxes.F90                        
  MOD_GroundTemperature.F90                   
  MOD_LeafInterception.F90                    
  MOD_NetSolar.F90                            
  MOD_WetBulb.F90                             
  MOD_RainSnowTemp.F90                        
  MOD_SoilSurfaceResistance.F90               
  MOD_NewSnow.F90                             
  MOD_Thermal.F90                             
  MOD_LightningData.F90                       
  CoLMDRIVER.F90                              
  CoLMMAIN.F90                                
  CoLM.F90
  ./coupling/pf_readout.F90
  ./coupling/pf_couple.F90
  ./coupling/pf_getforce.F90
  ./coupling/drv_g2clm.F90
  ./coupling/drv_gridmodule.F90
  ./coupling/drv_readvegtf.F90
  )

include_directories(./include)
#set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -M${CMAKE_CURRENT_BINARY_DIR}")

add_library(pfclm ${SRC_FILES})

install (TARGETS pfclm DESTINATION lib)
