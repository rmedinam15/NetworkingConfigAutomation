# NetworkingConfigAutomation

## [English version]:
This script performs the same configuration on the network equipment between **switch and router** of the manufacturer **Cisco** indicated by the user. The input must be a list of IPS.

The command must be exposed in the session with comment "**Comando único**". 

For example: 
```python
out = ssh.send_command("sh cdp neighbors")
```

## [Versión español]:
El presente script realiza una misma configuración en los equipos de red entre **switch y router** del fabricante **Cisco** indicados por el usuario. El input debe ser una lista de IPS.

El comando debe ser expuesto en la sesión con comentario "**Comando único**" 

Por ejemplo: 
```python
out = ssh.send_command("sh cdp neighbors")
```
