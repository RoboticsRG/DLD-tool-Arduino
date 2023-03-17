from droidbot.utils import md5
from droidbot.app import App
from droidbot.input_policy import DataLossPolicy
app_path = "/home/davi/Downloads/motog30/app_candidato/com.appmindlab.nano_1215.apk"
output_dir = "/home/davi/Downloads/motog30/reads"
app = App(app_path, output_dir=output_dir)
activity_list = DataLossPolicy.get_activity_list(app)

print(len(activity_list))

for i in activity_list:
    print(i)
# IntentEvent(intent='am start ru.evgeniy.dpitunnel/ru.evgeniy.dpitunnel.MainActivity') 8fe8a89ddb5a570cbf694cb4139023a7
state_str = md5("[{'unique_code': 'e9086b2f0b36f5ba8d29c2256d427d6d', 'triggered': False}, {'unique_code': 'e8f7eaf986d44663fd8e88e5d98c4cc5', 'triggered': False}, {'unique_code': 'e216103ecbfa85b2f632b5c2873d9745', 'triggered': False}, {'unique_code': '52ac0b17238d391d9596ac1c4e92dcf1', 'triggered': False}, {'unique_code': '84293c6131e4ef4986c376cf1f765a00', 'triggered': False}, {'unique_code': '561485186c4464512e3df499d0df4808', 'triggered': False}, {'unique_code': '485aa03c6709d4eefcff8a130dde053c', 'triggered': False}, {'unique_code': 'af83227e40a351fa86920f3294493816', 'triggered': False}, {'unique_code': 'c2abd63b5fea87aa7f4761b419cd6d66', 'triggered': False}, {'unique_code': 'b8aa06da6a9edd68e5c030fd2cc7b3e5', 'triggered': False}, {'unique_code': 'c2291f7f128a22a5e8e2ba02d1278c65', 'triggered': False}, {'unique_code': 'd586abd63f04d456c06422fcbe17f3ad', 'triggered': False}, {'unique_code': 'a2dc4f9b0a5b4ff77cef8a39f592dea9', 'triggered': False}, {'unique_code': '0d1a7dd90dc6402dcba19d46e9a845c6', 'triggered': False}, {'unique_code': '136ddceb45f86ef4d5136afdac1b7695', 'triggered': False}, {'unique_code': 'f65090fce13c4a69fb4ae05fdcb086d4', 'triggered': False}, {'unique_code': '2bad29719ad77ed7c8511bb1268b240d', 'triggered': False}, {'unique_code': '5b0e851efaece7f44d35211e9171b5b4', 'triggered': False}, {'unique_code': '5a6c9e6600d7eb9cdc8a7b120161d992', 'triggered': False}, {'unique_code': '71093029524d49fbfa7cfe58145bb533', 'triggered': False}, {'unique_code': '4bd37bdf98a50cd66dff68c424ef9a0f', 'triggered': False}, {'unique_code': '5794c03ecec83f63d2d61adbddfc122d', 'triggered': False}, {'unique_code': '23f0b9df48b3de70f769fd72068ab628', 'triggered': False}, {'unique_code': '756d3c42f834090f60e83bd181cd3eb4', 'triggered': False}, {'unique_code': 'e8c81ffeb81e6871c31737bf8ae58616', 'triggered': False}, {'unique_code': 'b54904020e01cf857c202a880f3b59d4', 'triggered': False}, {'unique_code': 'ef902defb416702f75df59e1e65d87c2', 'triggered': False}, {'unique_code': 'f9abc7090207ff9f2427ba47ad792a44', 'triggered': False}, {'unique_code': '9a2d30aa3cc23e2b1f9bc6b6b39fd029', 'triggered': False}, {'unique_code': '3bef84b0e4b1cc89b70f39e1759ece48', 'triggered': False}, {'unique_code': '0fe6c41b27a5e1859a6534fc08257d03', 'triggered': False}, {'unique_code': '35764413a874039f4c2c95f54ff311a2', 'triggered': False}, {'unique_code': 'f45d3baf41ec9270abc18b20e4cc60a6', 'triggered': False}, {'unique_code': 'bb8e111004661ec30643fd5d5d8577e2', 'triggered': False}, {'unique_code': 'fd82121c6997246f8dbefd0b3338454b', 'triggered': False}, {'unique_code': '3bbabf91b692a360e05db2c2c7bfa34b', 'triggered': False}, {'unique_code': '67613891855b856b03f547ec11c94f60', 'triggered': False}, {'unique_code': '10390703b400d0912257c438090a02bf', 'triggered': False}, {'unique_code': 'ddc85210ca5f9fcefcb434beb70231ca', 'triggered': False}, {'unique_code': None, 'triggered': False}, {'unique_code': None, 'triggered': False}, {'unique_code': None, 'triggered': False}, {'unique_code': None, 'triggered': False}, {'unique_code': '8fcf41ef0b7aa66ef1c50d762a9059d9', 'triggered': False}, {'unique_code': '047de7fd97a08e141dae158b6d932a2d', 'triggered': False}, {'unique_code': '8020e3834e021b3d41cb689f67a111ef', 'triggered': False}, {'unique_code': '892ca5c70b1c2ac2ae673a3909091758', 'triggered': False}, {'unique_code': 'b7ed4ea8d041e96a7b5243fc6479e8f1', 'triggered': False}, {'unique_code': 'd2f5435e57c007d73f5663b6f834acf6', 'triggered': False}, {'unique_code': '9da4b45f6f2631e60a7d5f8b975a1b98', 'triggered': False}, {'unique_code': '6b4506981c5c0dc5ca373de31b4d4f9d', 'triggered': False}, {'unique_code': '281470707ddc8415594845510dface04', 'triggered': False}, {'unique_code': 'dcee61d53051cae8eac5d17d89df2fab', 'triggered': False}, {'unique_code': 'f3905eb815e67aebc4e35617c9f0d5c2', 'triggered': False}, {'unique_code': 'bdea861e5c0f34327612cd18925afee7', 'triggered': False}, {'unique_code': 'fee7f3fa186b45f9ae518d760c5c7c5d', 'triggered': False}, {'unique_code': '6288a0a019d115b4b409bf076039c9cb', 'triggered': False}, {'unique_code': '537dbd9845f2ccce25c5910de1dcc80e', 'triggered': False}, {'unique_code': '1099b6fac5f6200fea7e0ebc888698da', 'triggered': False}, {'unique_code': '68b6a9c919f338d30f239a05a445df6e', 'triggered': False}, {'unique_code': 'c6725a8a81f58cda64d65a4b7f61d136', 'triggered': False}, {'unique_code': 'bf9f884d49f0753a8fc2ab30716b68e5', 'triggered': False}, {'unique_code': '57cbc11898edcda53ee89f89f7c66ccd', 'triggered': True}]")
# 9ed50e1420273f764ef1e0bce1c8dc96
print(state_str)



state_str = md5("[{'unique_code': 'e9086b2f0b36f5ba8d29c2256d427d6d', 'triggered': False}, {'unique_code': 'e8f7eaf986d44663fd8e88e5d98c4cc5', 'triggered': False}, {'unique_code': '41f694eb37cb02f255e3a7c73b2e9726', 'triggered': False}, {'unique_code': 'f0d572a6917b9635e9bbf876bf1a0487', 'triggered': False}, {'unique_code': '84293c6131e4ef4986c376cf1f765a00', 'triggered': False}, {'unique_code': '677d45aaef1255dbe8e302c6f7588773', 'triggered': False}, {'unique_code': 'ebda86097e4997e447090e28286060e3', 'triggered': False}, {'unique_code': 'a2d4619981f2ba6baed9574a2b328f40', 'triggered': False}, {'unique_code': 'c2abd63b5fea87aa7f4761b419cd6d66', 'triggered': False}, {'unique_code': '8f19d2260e443b3cdfa947b9576a7b94', 'triggered': False}, {'unique_code': '28482104c3c51ae32e76225b3feb6a11', 'triggered': False}, {'unique_code': '6c0db96e4b65dcbde649dda8f56544d0', 'triggered': False}, {'unique_code': '0f0eca43a74da05de7b3879ca23a3aac', 'triggered': False}, {'unique_code': 'bc849dd323fde7a847decfc565d77570', 'triggered': False}, {'unique_code': '1d587ca1daea05a54e74acda3077cb2d', 'triggered': False}, {'unique_code': 'd2e5355bc16ec29a11acbe0d9ab3d6e0', 'triggered': False}, {'unique_code': '3b63d5a26760cb4c95cda7086855c810', 'triggered': False}, {'unique_code': 'b1e60a349e111f10413838cb1dd93906', 'triggered': False}, {'unique_code': '11549f2614ce2f2244ba95a19f455bb8', 'triggered': False}, {'unique_code': '53a547c8f6f2e43af1a453144f4f837a', 'triggered': False}, {'unique_code': '1086c324bcffffdb7ace38c44209771c', 'triggered': False}, {'unique_code': '9a149e61ae69050d74e7b405c0e154ed', 'triggered': False}, {'unique_code': 'cacc010f67baae95fc96de6c55ddb05c', 'triggered': False}, {'unique_code': '9911224b0f5e67dd5ac0588bb2a6d539', 'triggered': False}, {'unique_code': 'd56a2227616ab8094fe80bdb1686d05a', 'triggered': False}, {'unique_code': 'b54904020e01cf857c202a880f3b59d4', 'triggered': False}, {'unique_code': 'f806706b32c356080d354f05c783d223', 'triggered': False}, {'unique_code': '22371f1706c6673ed800045f2d1ca3ce', 'triggered': False}, {'unique_code': 'c34f82463a98319b5b354aa5ac7b1d70', 'triggered': False}, {'unique_code': '3bef84b0e4b1cc89b70f39e1759ece48', 'triggered': False}, {'unique_code': 'bb2d501805656f229361c58d85d1c53c', 'triggered': False}, {'unique_code': '35764413a874039f4c2c95f54ff311a2', 'triggered': False}, {'unique_code': 'e38564c025f97639dc983d647dbc9643', 'triggered': False}, {'unique_code': '0e0643d4f8ee9106cee6ffc31919daae', 'triggered': False}, {'unique_code': 'fd82121c6997246f8dbefd0b3338454b', 'triggered': False}, {'unique_code': '29a951dbb10c68e1962b7fa9ae5f9f64', 'triggered': False}, {'unique_code': '05d516645e8af2c252ba14f7431f5734', 'triggered': False}, {'unique_code': '08296af8925cf9e093f752d0c2e77e1d', 'triggered': False}, {'unique_code': '85a94cf1b762db788a05ba31573da37a', 'triggered': False}, {'unique_code': '09248670adc56358eb755c855a2851f0', 'triggered': False}, {'unique_code': 'b7b82afce98c28b9342394b539d42f6f', 'triggered': False}, {'unique_code': '3c13012741e7ea66896545687f5abbf9', 'triggered': False}, {'unique_code': '808faf955e139b7ce66b73044d69ccf6', 'triggered': False}, {'unique_code': '4ddb63e63ffd7186a0df6ab95257a04d', 'triggered': False}, {'unique_code': 'da0db0c9f7b3e71f17df4e7980380747', 'triggered': False}, {'unique_code': '122b8c98f061d9aaf0dbe83c95f50dd7', 'triggered': False}, {'unique_code': '556367230e35a649e6191d7537bccc88', 'triggered': False}, {'unique_code': '7fee1c620e70d40c448dd78db7be88a8', 'triggered': False}, {'unique_code': '5a63ad32c20b276d87196934f5403fcf', 'triggered': False}, {'unique_code': '2a57076490fbff4de02af21ab4c9208f', 'triggered': False}, {'unique_code': 'b6becb00ba388ccdbc846abc015cac2f', 'triggered': False}, {'unique_code': '44eb16235f84e21ae5dcbcf8e6a0eefc', 'triggered': False}, {'unique_code': '39dfc05f6318b377a1120bf827fa4fff', 'triggered': False}, {'unique_code': '98d4e36b96b25421cec429179c21806e', 'triggered': False}, {'unique_code': 'e97b0d75384443134e39f70a42c0dd46', 'triggered': False}, {'unique_code': '1752653070303f26e22ad1a3456072c5', 'triggered': False}, {'unique_code': '237f14ee6ab4a204bb95741cefb24dfe', 'triggered': False}, {'unique_code': '88210e5195d155525f63f74a7a271dd6', 'triggered': False}, {'unique_code': '70e6a7e7819eb9e67eeefddbe572bb37', 'triggered': False}, {'unique_code': '9e9c8ab10eebd7a9fcd4a9967803e55b', 'triggered': False}, {'unique_code': 'da433867d2c705bf545c71a8d51e0c61', 'triggered': False}, {'unique_code': 'e8de7a988c038849529269ee0623e9d9', 'triggered': False}, {'unique_code': '7cca4f79809534e870d203a8fb94e3f7', 'triggered': False}, {'unique_code': 'd8954768c026f5f0eb5e4ddaf62a95fc', 'triggered': False}, {'unique_code': '0bcac8049b8bb4eed5d4e0faa2dd867f', 'triggered': False}, {'unique_code': 'c2161ddb10d937ecaa51c3cb14e2f4e7', 'triggered': False}, {'unique_code': '6a66c42ca5fdccd2969fc31b8448e13e', 'triggered': False}, {'unique_code': '6fa361c8d08c7a297148cf20b44878ea', 'triggered': False}, {'unique_code': '28b36492314672b9f26d0f58c5508d2c', 'triggered': False}, {'unique_code': '3c1648b4a68fa4b719fb2dc52e265aa6', 'triggered': False}, {'unique_code': 'b2c928006252085ba2231f84ec21e2c3', 'triggered': False}, {'unique_code': '68b6a9c919f338d30f239a05a445df6e', 'triggered': False}, {'unique_code': 'c6725a8a81f58cda64d65a4b7f61d136', 'triggered': False}, {'unique_code': 'bf9f884d49f0753a8fc2ab30716b68e5', 'triggered': False}, {'unique_code': '57cbc11898edcda53ee89f89f7c66ccd', 'triggered': True}]")
# 7ad4e42f9d92f65c461ea85086de1378
print(state_str)


state_str = md5("[{'unique_code': 'e9086b2f0b36f5ba8d29c2256d427d6d', 'triggered': False}, {'unique_code': 'e8f7eaf986d44663fd8e88e5d98c4cc5', 'triggered': False}, {'unique_code': 'f9f08ab20f046cbdd65f640b486e3e53', 'triggered': False}, {'unique_code': 'f0d572a6917b9635e9bbf876bf1a0487', 'triggered': False}, {'unique_code': 'acc80a4895e6b75fc98cd4484ccefcde', 'triggered': False}, {'unique_code': '628781fd81814484fc3c289a473aa1ca', 'triggered': False}, {'unique_code': 'ff576f8b04304e854059e8667cd74c92', 'triggered': False}, {'unique_code': 'dabcb09d3a151558c4bbb48401fbdd8e', 'triggered': False}, {'unique_code': '00e6e8d2e4b50de2c9b6ffc5e5e4c386', 'triggered': False}, {'unique_code': '8d44bd9c349eb75e345a1f908a40b2cc', 'triggered': False}, {'unique_code': 'c2291f7f128a22a5e8e2ba02d1278c65', 'triggered': False}, {'unique_code': 'e28acece53ec9de164729ffd58df0b92', 'triggered': False}, {'unique_code': '78798bf5f442369cf3cb9a5091c2c9dd', 'triggered': False}, {'unique_code': 'faa6bed2b8a2ef6a214fa752d53afebf', 'triggered': False}, {'unique_code': 'a7412ddeb1f90731159ae889b970caf0', 'triggered': False}, {'unique_code': '5c9a8aa67290033f68fff9d76fae6bb7', 'triggered': False}, {'unique_code': '3310dae92ee7f818c7e012506020ecec', 'triggered': False}, {'unique_code': 'fcbc6b06925d35d466023d076e5b44a1', 'triggered': False}, {'unique_code': '11549f2614ce2f2244ba95a19f455bb8', 'triggered': False}, {'unique_code': '53a547c8f6f2e43af1a453144f4f837a', 'triggered': False}, {'unique_code': '17664f80d55ed1956f98881d84dc2635', 'triggered': False}, {'unique_code': '9a149e61ae69050d74e7b405c0e154ed', 'triggered': False}, {'unique_code': '220294b1913155014955563b577af09f', 'triggered': False}, {'unique_code': '750ac09440c6054d4075e1b66d80d1ab', 'triggered': False}, {'unique_code': 'd56a2227616ab8094fe80bdb1686d05a', 'triggered': False}, {'unique_code': 'b54904020e01cf857c202a880f3b59d4', 'triggered': False}, {'unique_code': 'f806706b32c356080d354f05c783d223', 'triggered': False}, {'unique_code': 'a73e01358a8c55a7c021e0aaccdcb2ba', 'triggered': False}, {'unique_code': 'e9eb532f2934b5bf9279ec6407d613ca', 'triggered': False}, {'unique_code': '3bef84b0e4b1cc89b70f39e1759ece48', 'triggered': False}, {'unique_code': None, 'triggered': False}, {'unique_code': None, 'triggered': False}, {'unique_code': None, 'triggered': False}, {'unique_code': None, 'triggered': False}, {'unique_code': '1806e88210b99332440ab6116eee07fe', 'triggered': False}, {'unique_code': '1921a036ef378e33437384e35fce87c0', 'triggered': False}, {'unique_code': '3559c97d8e7d7d80386bd2b890f2b221', 'triggered': False}, {'unique_code': '6d7dc515c38d99105bec62bb96e3c2ba', 'triggered': False}, {'unique_code': 'ba76975d88b9acdb369c36da00a2559b', 'triggered': False}, {'unique_code': 'bc22351bc04aaac52dc53720b7d398d8', 'triggered': False}, {'unique_code': 'f1a154a60b975815038ba745ce721987', 'triggered': False}, {'unique_code': '141ecd309a5a63c780a83063ebac97d2', 'triggered': False}, {'unique_code': '721136a328f552168960985ddd39e45c', 'triggered': False}, {'unique_code': '68b6a9c919f338d30f239a05a445df6e', 'triggered': False}, {'unique_code': 'c6725a8a81f58cda64d65a4b7f61d136', 'triggered': False}, {'unique_code': 'bf9f884d49f0753a8fc2ab30716b68e5', 'triggered': False}, {'unique_code': '57cbc11898edcda53ee89f89f7c66ccd', 'triggered': True}]")
# dd75a1b745ecaa1b79bdea5cb308dd9f
print(state_str)


state_str = md5("")
# d41d8cd98f00b204e9800998ecf8427e
print(state_str)

