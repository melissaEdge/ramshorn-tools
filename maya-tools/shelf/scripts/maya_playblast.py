import maya_geo_export as geo
import utilities as amu
import maya.cmds as mc
import maya.mel as mel
import os

def simpleBlast(name, startFrame, endFrame):

    currentPanel = mc.getPanel(wf=True)
    currentCamera = mc.modelEditor(currentPanel, q=True, camera=True)

    panelSwitch = []
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, nc=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, ns=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, pm=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, sds=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, pl=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, lt=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, ca=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, j=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, ikh=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, df=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, dy=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, fl=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, hs=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, fo=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, lc=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, dim=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, ha=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, pv=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, tx=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, str=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, gr=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, cv=True))
    panelSwitch.append(mc.modelEditor(currentPanel, q=True, hu=True))

    mel.eval("lookThroughModelPanel "+currentCamera+" "+currentPanel)
    mc.modelEditor(currentPanel, e=True, allObjects=0)
    mc.modelEditor(currentPanel, e=True, polymeshes=1)
    mc.modelEditor(currentPanel, e=True, nurbsSurfaces=0)
    mc.modelEditor(currentPanel, e=True, strokes=1)
    mc.modelEditor(currentPanel, e=True, cameras=0)

    playback_slider = mel.eval('$tmpVar=$gPlayBackSlider')
    soundfile = mc.timeControl(playback_slider, q=True, sound=True)
    print soundfile

    mc.playblast(st=startFrame, et=endFrame, sound=soundfile, fmt="qt", compression="jpeg", qlt=100, forceOverwrite=True, filename=name,
                 width=1280, height=692, offScreen=True, percent=100, v=False)

    mel.eval("lookThroughModelPanel "+currentCamera+" "+currentPanel)
    mc.modelEditor(currentPanel, e=True, nc=panelSwitch[0])
    mc.modelEditor(currentPanel, e=True, ns=panelSwitch[1])
    mc.modelEditor(currentPanel, e=True, pm=panelSwitch[2])
    mc.modelEditor(currentPanel, e=True, sds=panelSwitch[3])
    mc.modelEditor(currentPanel, e=True, pl=panelSwitch[4])
    mc.modelEditor(currentPanel, e=True, lt=panelSwitch[5])
    mc.modelEditor(currentPanel, e=True, ca=panelSwitch[6])
    mc.modelEditor(currentPanel, e=True, j=panelSwitch[7])
    mc.modelEditor(currentPanel, e=True, ikh=panelSwitch[8])
    mc.modelEditor(currentPanel, e=True, df=panelSwitch[9])
    mc.modelEditor(currentPanel, e=True, dy=panelSwitch[10])
    mc.modelEditor(currentPanel, e=True, fl=panelSwitch[11])
    mc.modelEditor(currentPanel, e=True, hs=panelSwitch[12])
    mc.modelEditor(currentPanel, e=True, fo=panelSwitch[13])
    mc.modelEditor(currentPanel, e=True, lc=panelSwitch[14])
    mc.modelEditor(currentPanel, e=True, dim=panelSwitch[15])
    mc.modelEditor(currentPanel, e=True, ha=panelSwitch[16])
    mc.modelEditor(currentPanel, e=True, pv=panelSwitch[17])
    mc.modelEditor(currentPanel, e=True, tx=panelSwitch[18])
    mc.modelEditor(currentPanel, e=True, str=panelSwitch[19])
    mc.modelEditor(currentPanel, e=True, gr=panelSwitch[20])
    mc.modelEditor(currentPanel, e=True, cv=panelSwitch[21])
    mc.modelEditor(currentPanel, e=True, hu=panelSwitch[22])

    djv_cmd = (" /usr/local/djv/bin/djv_view  " + name +  ".mov &");
    os.system(djv_cmd)
    print "playblast saved here: "+name+".mov"

def glBlast(name, startFrame, endFrame):
    mc.setAttr('defaultHardwareRenderGlobals.filename', name, type="string")
    #image settings
    mc.setAttr('defaultHardwareRenderGlobals.startFrame', startFrame)
    mc.setAttr('defaultHardwareRenderGlobals.endFrame', endFrame)
    mc.setAttr('defaultHardwareRenderGlobals.extension', 4)
    mc.setAttr('defaultHardwareRenderGlobals.imageFormat', 8)
    mc.setAttr('defaultHardwareRenderGlobals.fullImageResolution', 1)
    mc.setAttr('defaultHardwareRenderGlobals.resolution', 'HD576 1024 576 1.778',  type='string')
    mc.setAttr('defaultHardwareRenderGlobals.backgroundColor', 0.5, 0.5, 0.5, type='double3')
    #motion blur
    mc.setAttr('defaultHardwareRenderGlobals.edgeSmoothing', 1)
    mc.setAttr('defaultHardwareRenderGlobals.lineSmoothing', 1)
    mc.setAttr('defaultHardwareRenderGlobals.multiPassRendering', 1)
    mc.setAttr('defaultHardwareRenderGlobals.renderPasses', 5)
    mc.setAttr('defaultHardwareRenderGlobals.antiAliasPolygons', 1)
    mc.setAttr('defaultHardwareRenderGlobals.motionBlur', 0.5)
    mc.setAttr('defaultHardwareRenderGlobals.backgroundColor', 0.5, 0.5, 0.5, type='double3')
    #lighting
    mc.setAttr('defaultHardwareRenderGlobals.lightingMode', 1)
    mc.setAttr('defaultHardwareRenderGlobals.drawStyle', 3)
    mc.setAttr('defaultHardwareRenderGlobals.texturing', 1)

    currentPanel = mc.getPanel(wf=True)
    currentCamera = mc.modelEditor(currentPanel, q=True, camera=True)
    
    #=========================BROKEN RIGHT NOW=========================
    glWindow = mc.window()
    mc.paneLayout()
    mc.glRenderEditor(lookThru=currentCamera)
    mc.showWindow(glWindow)
    # mc.glRender(glWindow, renderSequence=True)
    #=========================BROKEN RIGHT NOW=========================
    
    print "playblast saved here: "+name+".mov"

    mc.confirmDialog(title = 'Error'
                        , message       = 'Doesn\'t work yet!'
                        , button        = ['Ok']
                        , defaultButton = 'Ok'
                        , cancelButton  = 'Ok'
                        , dismissString = 'Ok')

def showErrorDialog():
    return mc.confirmDialog(title = 'Error'
                        , message       = 'This is not an animation file!'
                        , button        = ['Ok']
                        , defaultButton = 'Ok'
                        , cancelButton  = 'Ok'
                        , dismissString = 'Ok')
    

def go():
    try:
        assetName, assetType, version = geo.decodeFileName()
    except IndexError:
        showErrorDialog()
        return

    if not assetType == 'animation':
        showErrorDialog()
        return

    fileName = mc.file(q=True, sceneName=True)
    dirName = os.path.dirname(fileName)
    source = amu.getCheckinDest(dirName)
    blastPath = os.path.join(os.path.dirname(source), 'playblasts')
    versionNum = amu.getLatestVersion(source)+1
    name = os.path.join(blastPath, assetName+"_v"+("%03d" % versionNum))

    startFrame = mc.playbackOptions(q=True, min=True)
    endFrame = mc.playbackOptions(q=True, max=True)

    choice = mc.confirmDialog( title = 'Playblast Tool'
                              , message       = 'What kind of playblast?'
                              , button        = ['Cancel', 'GL', 'Simple']
                              , defaultButton = 'Simple'
                              , cancelButton  = 'Cancel'
                              , dismissString = 'Cancel')
    if choice == 'Simple':
        simpleBlast(name, startFrame, endFrame)
    elif choice == 'GL':
        glBlast(name, startFrame, endFrame)

if __name__ == '__main__':
    go()
