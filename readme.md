# Pythoid

Pythoid is a Java mod for the game `Project Zomboid` that integrates the `Jython 2.7.3` 
interpreter to Java, enabling Python support for modding the game. Pythoid ships utilities that aids
in integration of Python-built classes with Lua's ability to both see and invoke.

# Pythoid-Typings

Pythoid-Typings is a vscode-based set of typings exposing Project Zomboid's Java environment. It
casts a large net, exposing Project Zomboid's Java environment for Python mods to see what they can
modify & use. It is not complete however all PZ-written classes are currently exposed. Opportunities
exist for writing a full-exposure of third-party libraries. This is an on-going project.

# Global Typings Configuration

Create a `.vscode/settings.json` file. Add this setting:
```json
{
    "python.analysis.stubPath": "Path/To/Pythoid-Typings",
}
```

# Note:

Due to a recent update, Pylance no longer resolves imports with folders named the same as `.pyi`
files so downgrade your Pylance extension to version `2024.7.1` in order to use these typings. If
you don't know how to do this, go to your extensions tab on the left-side of the vscode window, look
up `Pylance`, and right-click it to install the correct version.

# Support

![](https://i.imgur.com/ZLnfTK4.png)

# Discord Server

<https://discord.gg/u3vWvcPX8f>