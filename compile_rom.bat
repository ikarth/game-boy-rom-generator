@if (@CodeSection == @Batch) @then
@echo off
echo compiling %1
echo project: %2

rem This is a really hacky way to do it, but I'm not going to bother
rem with anything fancier for version 1.0 of the generator.

set SendKeys=CScript //nologo //E:JScript "%~F0" %2


start "GB Studio Compiling" J:\Isaac\Dev\genboy\gbstudio\gb-studio.exe %1

echo Waiting for GB Studio to start...
ping -n 5 -w 1 127.0.0.1 > NUL

%SendKeys% "^7"

ping -n 3 -w 1 127.0.0.1 > NUL

%SendKeys% "+^N"
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
WScript.Sleep(10);
if(WshShell.AppActivate("GB Studio")) {
  WshShell.SendKeys(WScript.Arguments(0));
} else {
  if(WshShell.AppActivate(WScript.Arguments(1))) {
    WshShell.SendKeys(WScript.Arguments(0));
  } else {
    WScript.Echo("Failed to activate GB Studio");
    WScript.Quit(1);
  }
}
