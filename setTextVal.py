import maya.cmds as cmds
def setTextVal(typeNode, textString):
    hexValues = []
    for character in textString:
        hexValues.append(character.encode('hex'))
    attrVal = ' '.join(hexValues)
    cmds.setAttr(typeNode+'.textInput', attrVal, type='string')