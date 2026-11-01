"""Build FFIV Trilogy Beta 1.1 from three user-supplied original ROMs (Python 3)."""
from pathlib import Path
import hashlib,json,sys
HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def build(paths,output):
 m=json.loads((HERE/'manifest.json').read_text());roms=[]
 for path,entry in zip(paths,m['sources']):
  b=Path(path).read_bytes()
  if len(b)!=entry['bytes'] or sha(b)!=entry['sha256']:raise ValueError('Wrong source for '+entry['name']+'. Expected SHA-256 '+entry['sha256'])
  roms.append(b)
 base=bytearray(bytes(16+1048576)+b''.join(b[16:] for b in roms))
 if sha(base)!=m['assembledBaseSha256']:raise ValueError('Assembly checksum failed')
 patch=(HERE/'trilogy.ips').read_bytes()
 if sha(patch)!=m['patchSha256'] or patch[:5]!=b'PATCH':raise ValueError('Patch checksum failed')
 i=5
 while patch[i:i+3]!=b'EOF':
  off=int.from_bytes(patch[i:i+3],'big');n=int.from_bytes(patch[i+3:i+5],'big');i+=5
  if n:data=patch[i:i+n];i+=n
  else:n=int.from_bytes(patch[i:i+2],'big');data=patch[i+2:i+3]*n;i+=3
  if len(data)!=n or off+n>len(base):raise ValueError('Invalid patch record')
  base[off:off+n]=data
 if len(base)!=m['outputBytes'] or sha(base)!=m['outputSha256']:raise ValueError('Output checksum failed')
 with Path(output).open('xb') as f:f.write(base)
 print('Created '+str(output)+'\nSHA-256: '+sha(base))
if __name__=='__main__':
 if len(sys.argv)!=5:sys.exit('Usage: python patch.py X1.nes X2.nes X3.nes output.nes')
 try:build(sys.argv[1:4],sys.argv[4])
 except (OSError,ValueError) as e:sys.exit('Error: '+str(e))
