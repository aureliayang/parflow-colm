!#include <misc.h>

subroutine drv_g2clm(grid,nx,ny,planar_mask,numpatch)

!=========================================================================
!
!  CLMCLMCLMCLMCLMCLMCLMCLMCL  A community developed and sponsored, freely   
!  L                        M  available land surface process model.  
!  M --COMMON LAND MODEL--  C  
!  C                        L  CLM WEB INFO: http://clm.gsfc.nasa.gov
!  LMCLMCLMCLMCLMCLMCLMCLMCLM  CLM ListServ/Mailing List: 
!
!=========================================================================
! DESCRIPTION:
!  Transfer variables into CLM tile space from grid space. 
!
! REVISION HISTORY:
!  15 Jan 2000: Paul Houser; Initial code
!=========================================================================
! $Id: drv_g2clm.F90,v 1.1.1.1 2006/02/14 23:05:52 kollet Exp $
!=========================================================================

  use MOD_Precision
  !use drv_module          ! 1-D Land Model Driver variables
  !use drv_tilemodule      ! Tile-space variables
  use drv_gridmodule      ! Grid-space variables
  !use clmtype             ! CLM tile variables
  !use clm_varcon, only : istdlak, istslak
  use MOD_Vars_TimeInvariants
  implicit none

!=== Arguments ===========================================================

  !type (drvdec)  :: drv              
  !type (tiledec) :: tile
  integer  :: nx, ny 
  type (griddec) :: grid(nx,ny)   
  !type (clm1d)   :: clm

!=== Local Variables =====================================================

  integer  :: r,c,t       ! Loop counters
  integer  :: numpatch
  integer  :: planar_mask(3,nx*ny)

!=== End Variable Definition =============================================

!=== Transfer variables that are identical for each tile in a grid 
!===  to tile space  - for some aplications, the assumption
!===  of spatially constant information across a grid for these
!===  variables may be incorrect, and should be modified by the user.

  do t = 1, numpatch

      c = planar_mask(1,t)
      r = planar_mask(2,t)

      !htoplc(t)         = grid(c,r)%htoplc 
      patchclass(t)     = grid(c,r)%patchclass
      patchlatr(t)      = grid(c,r)%patchlatr*4.*atan(1.)/180.  
      patchlonr(t)      = grid(c,r)%patchlonr*4.*atan(1.)/180.
      !vf_quartz(:,t)    = grid(c,r)%vf_quartz(:)
      vf_gravels(:,t)   = grid(c,r)%vf_gravels(:)
      vf_om(:,t)        = grid(c,r)%vf_om(:)
      vf_sand(:,t)      = grid(c,r)%vf_sand(:)
      wf_gravels(:,t)   = grid(c,r)%wf_gravels(:)
      wf_sand(:,t)      = grid(c,r)%wf_sand(:)
      !psi0(:,t)         = grid(c,r)%psi0(:)
      !bsw(:,t)          = grid(c,r)%bsw(:)
      !theta_r(:,t)      = grid(c,r)%theta_r(:)  
      !alpha_vgm(:,t)    = grid(c,r)%alpha_vgm(:)
      !n_vgm(:,t)        = grid(c,r)%n_vgm(:)
      !L_vgm(:,t)        = grid(c,r)%L_vgm(:)
      !hksati(:,t)       = grid(c,r)%hksati(:)
      csol(:,t)         = grid(c,r)%csol(:)
      k_solids(:,t)     = grid(c,r)%k_solids(:)
      dksatu(:,t)       = grid(c,r)%dksatu(:)
      dksatf(:,t)       = grid(c,r)%dksatf(:)
      dkdry(:,t)        = grid(c,r)%dkdry(:)
      !BA_alpha(:,t)     = grid(c,r)%BA_alpha(:)
      !BA_beta(:,t)      = grid(c,r)%BA_beta(:)
      !OM_density(:,t)   = grid(c,r)%OM_density(:)
      !BD_all(:,t)       = grid(c,r)%BD_all(:)

      WHERE ((vf_gravels(:,t) + vf_sand(:,t)) > 0.4)
        BA_alpha(:,t) = 0.38
        BA_beta(:,t) = 35.0
      ELSEWHERE ((vf_gravels(:,t) + vf_sand(:,t)) > 0.25)
        BA_alpha(:,t) = 0.24
        BA_beta(:,t) = 26.0
      ELSEWHERE
        BA_alpha(:,t) = 0.2
        BA_beta(:,t) = 10.0
      END WHERE

  enddo

  return
end subroutine drv_g2clm



