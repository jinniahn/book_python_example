from subprocess import call

class Lirc:
    def __init__(self, text):

        self.remos = {}
        
        # 리모콘 기기와 키를 분석한다.
        self.parse(text)

    def send_key(self, remo_name, button_name):
        cmd = 'irsend SEND_ONCE {} {}'.format(remo_name, button_name)
        call(cmd, shell=True)

    def get_remotes(self):
        return self.remos.keys()

    def get_buttons(self, remo_name):
        return self.remos[remo_name]

    def __str__(self):
        ret = []
        for remo_name in self.remos:
            ret.append("- {}".format(remo_name))
            for button in self.remos[remo_name]:
                ret.append("    - {}".format(button))
        
        return '\n'.join(ret)

    def parse(self, text):

        remo_name = None
        buttons   = []
        states = []   # '', 'remote', 'codes'

        for line in text.splitlines():
            line = line.replace('\t',' ').strip()
            
            if line.startswith('#'):
                continue
            # 초기화
            if line == 'begin remote':
                states.append('remote')
                buttons = []
                remo_name = None

            elif line == 'end remote':
                status = states.pop()
                assert status == 'remote'
                assert remo_name != None
                self.remos[remo_name] = buttons

            elif line == 'begin codes':
                states.append('codes')
                
            elif line == 'end codes':
                status = states.pop()
                assert status == 'codes'            
                
            elif line == 'begin raw_codes':
                states.append('raw_codes')
                
            elif line == 'end raw_codes':
                status = states.pop()
                assert status == 'raw_codes'            
                
            elif line.startswith('name'):
                tokens = list( map(str.strip, line.split(' ', 1)) )                    
                if states[-1] == 'raw_codes':
                    name = tokens[1]
                    buttons.append(name)
                    
                elif states[-1] == 'remote':
                    remo_name = tokens[1]
                    
            elif len(line) > 0:
                tokens = list( map(str.strip, line.split(' ', 1)) )
                if states[-1] == 'codes':
                    name = tokens[0]
                    buttons.append(name)



def test():
    text = '''\
begin remote

  name  tout1
  bits           16
  flags SPACE_ENC|CONST_LENGTH
  eps            30
  aeps          100

  header       8958  4506
  one           578  1652
  zero          578   579
  ptrail        579
  repeat       8963  2242
  pre_data_bits   16
  pre_data       0xFF
  gap          108097
  toggle_bit_mask 0x0

      begin codes
          t                        0x30CF
          2                        0x18E7
      end codes

end remote
    '''

    lirc = Lirc(text)
    print(lirc)

def test1():
    text = '''\
begin remote

  name  tv1
  flags RAW_CODES
  eps            30
  aeps          100

  gap          96202

      begin raw_codes

          name t
             8984    4488     597     551     579     602
              575     553     577     578     576     575
              580     577     577     605     550     574
              580    1654     580    1652     584    1654
              580    1665     570    1655     578    1653
              583    1655     578    1655     581     583
              573    1652     582    1657     579     576
              576    1657     578     577     589     566
              578     577     576    1656     579     577
              551     605     550    1678     582     578
              562    1670     554    1680     555    1679
              555   39554    8938    2263     551

          name t1
             8984    4488     597     551     579     602
              575     553     577     578     576     575
              580     577     577     605     550     574
              580    1654     580    1652     584    1654
              580    1665     570    1655     578    1653
              583    1655     578    1655     581     583
              573    1652     582    1657     579     576
              576    1657     578     577     589     566
              578     577     576    1656     579     577
              551     605     550    1678     582     578
              562    1670     554    1680     555    1679
              555   39554    8938    2263     551

      end raw_codes

end remote'''

    lirc = Lirc(text)
    print(lirc)

def test2():
    lirc = Lirc(open('./conf/lircd.conf').read())
    print(lirc)
    

if __name__ == '__main__':
    test2()
    
