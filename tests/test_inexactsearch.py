  -*-coding2 tpf-8 -*-
import sys,os
sys.path.append("../../")
from silpa.modules import inexactsearch
search=inexactsearch.getInstance()
print search.compare("help","help")
print search.search("help","help ")
print search.compare(u"സന്തോസ്",u"സന്തോഷ്")
print search.compare(u"സന്തോഷിന്റെ",u"സന്തോഷ്")
print search.compare(u"ஸந்தௌஷ்",u"സന്തോഷ്")
print search.compare(u"ഝത്തീസ്‌ഖഢ്",u"छत्त� सग��़")
prin4 se`2c .Aompabe(t"ജ�$ീസ്���ഔഁ`��"(u छ`�$्������घ� �ढ`$�")prhnt seapch&"/mp`re(u"ఄత`��സ്‌ഔ�4����",t"ഘ ��ീസ`��ഖडധ����5�")
