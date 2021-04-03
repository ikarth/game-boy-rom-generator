@if (@CodeSection == @Batch) @then
@echo off
echo compiling %1
echo project: %2

rem This is a really hacky way to do it, but I'm not going to bother
rem with anything fancier for version 1.0 of the generator.

set SendKeys=CScript //nologo //E:JScript "%~F0"


start "GB Studio" J:\Isaac\Dev\genboy\gbstudio\gb-studio.exe %1

echo Waiting for GB Studio to start...
rem ping -n 9 -w 1 127.0.0.1 > NUL

rem %SendKeys% "^7" %2 9000

rem ping -n 1 -w 1 127.0.0.1 > NUL

%SendKeys% "+^(N)" %2 8000
echo Compiling...

ping -n 30 -w 1 127.0.0.1 > NUL

echo Shutting down after 30 seconds...

rem powershell (get-process)
powershell (ps gb-studio).CloseMainWindow()


echo Finished compiling %1

goto :EOF

@end

// JScript section

var WshShell = WScript.CreateObject("WScript.Shell");
WScript.Sleep(WScript.Arguments.Item(2));
if(WshShell.AppActivate(WScript.Arguments.Item(1))) {

    WScript.Echo("Activated");
    WshShell.SendKeys(WScript.Arguments(0));
    WScript.Echo(WScript.Arguments.Item(0));
    WScript.Echo(WScript.Arguments.Item(1));
} else {
  if(WshShell.AppActivate("GB Studio")) {
      WshShell.SendKeys(WScript.Arguments.Item(0));
      WScript.Echo("Activated GB Studio");
  } else {
      WScript.Echo("Failed to activate GB Studio");
      WScript.Echo(WScript.Arguments.Item(0));
      WScript.Echo(WScript.Arguments.Item(1));
      WScript.Quit(1);
  }
}
