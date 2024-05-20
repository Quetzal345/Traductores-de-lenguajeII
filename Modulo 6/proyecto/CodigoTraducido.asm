.386
.model flat, stdcall
option casemap:none

include c:\masm32\include\masm32rt.inc

.code

suma proc a:DWORD,b:DWORD
mov eax, a
add eax, b
ret
suma endp

resta proc c:DWORDmov eax, c
sub eax, c
ret
resta endp

main proc
local resul1:DWORD
local resul2:DWORD
mov eax, 5
push eax
mov eax, 9
push eax
call suma
mov resul1, eax
mov eax, resul1
print str$(eax)
mov eax, resul1
push eax
call resta
mov resul2, eax
mov eax, resul2
print str$(eax)
invoke ExitProcess, 0

main endp
end main.386
.model flat, stdcall
option casemap:none

include c:\masm32\include\masm32rt.inc

.code

suma proc a:DWORD,b:DWORD
mov eax, a
add eax, b
ret
suma endp

resta proc c:DWORDmov eax, c
sub eax, c
ret
resta endp

main proc
local resul1:DWORD
local resul2:DWORD
mov eax, 5
push eax
mov eax, 9
push eax
call suma
mov resul1, eax
mov eax, resul1
print str$(eax)
mov eax, resul1
push eax
call resta
mov resul2, eax
mov eax, resul2
print str$(eax)
invoke ExitProcess, 0

main endp
end main