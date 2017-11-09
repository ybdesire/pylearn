#include <windows.h>
 
 
BOOL APIENTRY DllMain(HANDLE hModule, DWORD dwReason, LPVOID lpReserved)
{
    return TRUE;
}
 
__declspec(dllexport) int multiply(int num1, int num2)
{
    return num1 * num2;
}