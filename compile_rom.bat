@if (@CodeSection == @Batch) @then
@echo off
echo compiling %1
echo project: %2

rem This is a really hacky way to do it, but I'm not going to bother
rem with anything fancier for version 1.0 of the generator.

set SendKeys=CScript //nologo //E:JScript "%~F0"


start "GB Studio Compiling" J:\Isaac\Dev\genboy\gbstudio\gb-studio.exe %1

echo Waiting for GB Studio to start...
ping -n 8 -w 1 127.0.0.1 > NUL

%SendKeys% "^7" %2

ping -n 7 -w 1 127.0.0.1 > NUL

%SendKeys% "+^N" %2
echo Compiling...

ping -n 20 -w 1 127.0.0.1 > NUL

echo Shutting down after 20 seconds...

rem powershell (get-process)
powershell (ps gb-studio).CloseMainWindow()


echo Finished compiling %1

goto :EOF

@end

// JScript section

var WshShell = WScript.CreateObject("WScript.Shell");
WScript.Sleep(150);
if(WshShell.AppActivate("GB Studio")) {
  WScript.Sleep(150);
  WshShell.SendKeys(WScript.Arguments.Item(0));
  WScript.Echo("Activated GB Studio");
} else {
  if(WshShell.AppActivate(WScript.Arguments.Item(1))) {
    WScript.Echo("Activated");
    WScript.Sleep(150);
    WshShell.SendKeys(WScript.Arguments(0));
    WScript.Echo(WScript.Arguments.Item(0));
    WScript.Echo(WScript.Arguments.Item(1));
  } else {
    WScript.Echo("Failed to activate GB Studio");
    WScript.Echo(WScript.Arguments.Item(0));
    WScript.Echo(WScript.Arguments.Item(1));
    WScript.Quit(1);
  }
}
