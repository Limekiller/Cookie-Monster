start RunDll32-low.exe InetCpl.cpl,ClearMyTracksByProcess 6655
ping 127.0.0.1 -n 2 > nul
TASKKILL /F /IM rundll32-low.exe
