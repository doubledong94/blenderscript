import bpy
import os
from wf000script_data_structure import *
# from wf001script1 import scriptObj



scriptObj = [
    ["开场白","阅读Java代码时,众多变量的赋值与读取",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/puzzled.jpeg",TransitionType.NONE,Transform([1.918,1.918],[0,-370],0)],
    ["开场白","总让人化身狗熊掰棒子,看一个忘一个",False],
    ["开场白","众多函数的嵌套",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/engaged.jpg",TransitionType.FADE,Transform([1.918,1.918],[0,0],0)],
    ["开场白","总让人陷入迷宫,绞尽脑汁也无法找到出口",False],
    ["开场白","你是否也觉得",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/crazy.jpeg",TransitionType.FADE,Transform([1.918,1.918],[0,-115],0)],
    ["开场白","找一个变量值的最终来源与用途十分机械,繁琐",False],
    ["开场白","甚至侮辱程序员的智商",False],
    ["开场白","矢山代码阅读器应此而生",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/relieved.jpeg",TransitionType.FADE,Transform([1.918,1.918],[0,-131],0)],
# -----------------------------------------------------------
    ["简介","矢山基本介绍",True,SceneType.TEXT,"矢山基本介绍",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["简介","你眼中的赋值表达式",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/1assigntext.mp4",TransitionType.FADE,Transform([1.2,1.2],[621,-36],0),-100],
    ["简介","矢山展现的赋值表达式",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/2assignimg.mp4",TransitionType.WIPE,Transform([0.713,0.713],[0,0],0),-100],
    ["简介","你眼中的计算表达式",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/3calctext.mp4",TransitionType.FADE,Transform([1.038,1.038],[268,280],0),-100],
    ["简介","矢山展现的计算表达式",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/4calcimg.mp4",TransitionType.WIPE,Transform([0.821,0.821],[0,-40],0),-200],
    ["简介","你眼中的变量在循环中的使用",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/5looptext.mp4",TransitionType.FADE,Transform([1.153,1.153],[483,17],0),-100],
    ["简介","矢山展现的变量在循环中的使用",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/6loopimg.mp4",TransitionType.WIPE,Transform([0.69,0.69],[0,0],0),-100],
    ["简介","你眼中的条件语句",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/7iftext.mp4",TransitionType.FADE,Transform([1.055,1.055],[411,-206],0),-100],
    ["简介","矢山展现的条件语句",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/8ifimg.mp4",TransitionType.WIPE,Transform([0.687,0.687],[0,-40],0),-150],
    ["简介","你眼中的参数传递",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/9paramtext.mp4",TransitionType.FADE,Transform([1.159,1.159],[540,-150],0),-100],
    ["简介","矢山展现的参数传递",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/10paramimge.mp4",TransitionType.WIPE,Transform([0.73,0.73],[0,0],0),-100],
    ["简介","你眼中的对象引用",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/11reftext.mp4",TransitionType.FADE,Transform([1.2,1.2],[604,-60],0),-100],
    ["简介","矢山展现的对象引用",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/12refimg.mp4",TransitionType.WIPE,Transform([0.79,0.79],[0,0],0),-100],
    ["简介","矢山用正则搜索的方式",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/regular-expression-regex-regexp-in-linux.webp",TransitionType.FADE,Transform([1.678,1.678],[70,-12],0)],
    ["简介","图形化展示你所关注的数据流动,时机传递,逻辑控制和对象引用",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/graphicalcode.jpeg",TransitionType.WIPE,Transform([2.079,2.079],[-4,-100],0)],
    ["简介","当你想要了解一个变量最终被传递到哪里",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/13flowtotext.mp4",TransitionType.FADE,Transform([1.6,1.6],[1151,-145],0),-100,[[SceneType.IMG,"/home/ydd/Documents/shishan/resource/arrow.png",Transform([0.468,0.33],[-122,165],-3.07),0.1,0.9]]],
    ["简介","只需要将这个变量设置为自定义字符",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/14flowtochar.mp4",TransitionType.FADE,Transform([1.2,1.2],[722,-458],0),-40,[[SceneType.IMG,"/home/ydd/Documents/shishan/resource/arrow.png",Transform([0.313,0.313],[350,78],3.769),0.1,0.9]]],
    ["简介","然后在正则表达式中将这个自定义字符放在开头",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/15flowtoregex.mp4",TransitionType.FADE,Transform([1.347,1.347],[940,220],0),-80,[[SceneType.IMG,"/home/ydd/Documents/shishan/resource/arrow.png",Transform([0.313,0.313],[-58,97],3.769),0.1,0.9]]],
    ["简介","矢山就可以从这个变量开始搜索数据流动了",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/16flowtograph.mp4",TransitionType.WIPE,Transform([0.635,0.635],[0,0],0),-100],
    ["简介","除了自定义字符",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid60/15flowtoregex.mp4",TransitionType.FADE,Transform([1.168,1.168],[684,-13],0),-50,[[SceneType.COLOR,"",Transform([1.3,0.196],[0,-63],0),0.4,0.45],[SceneType.COLOR,"",Transform([1.3,0.196],[0,-63],0),0.5,0.55],[SceneType.COLOR,"",Transform([1.3,0.196],[0,-63],0),0.6,0.65],[SceneType.COLOR,"",Transform([1.3,0.196],[0,-63],0),0.7,0.75]]],
    ["简介","矢山还提供了以下内置的正则字符,方便用户编写正则表达式",False],
# -----------------------------------------------------------
    ["界面操作","界面操作",True,SceneType.TEXT,"界面操作",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作","下载编译与解析源码的教程请移步github搜索矢山",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/github.png",TransitionType.FADE,Transform([1.875,1.875],[0,0],0)],
    ["界面操作","完成矢山的下载编译与解析源码流程后",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid60/1compile.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-100],
    ["界面操作","就可以定义字符和编写正则了",False],
    ["界面操作","快捷键e打开正则编辑面板",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid60/2panelgeneral.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-320,[[SceneType.TEXT,"类范围列表",Transform([1,1],[537,321],0),0.3,0.9],[SceneType.TEXT,"自定义字符列表",Transform([1,1],[603,70],0),0.3,0.9],[SceneType.TEXT,"正则列表",Transform([1,1],[518,-297],0),0.3,0.9],[SceneType.IMG,"/home/ydd/Documents/shishan/resource/arrow.png",Transform([0.25,0.25],[204,316],-3.09),0.3,0.9],[SceneType.IMG,"/home/ydd/Documents/shishan/resource/arrow.png",Transform([0.25,0.25],[225,63],-3.09),0.3,0.9],[SceneType.IMG,"/home/ydd/Documents/shishan/resource/arrow.png",Transform([0.25,0.25],[212,-293],-3.09),0.3,0.9]]],
    ["界面操作","注意: 此面板中的大部分列表的元素都可以通过拖拽改变顺序",False],
    ["界面操作","通过双击进行编辑或者删除",False],
    ["界面操作","在讲每个列表时就不重复说明了",False],
# -----------------------------------------------------------
    ["界面操作/定义字符","自定义字符",True,SceneType.TEXT,"自定义字符",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作/定义字符","自定义字符可以通过指定具体的属性与函数生成",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/17customchar.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-60],
    ["界面操作/定义字符","也可以通过规则生成",False],
    ["界面操作/定义字符","右键列表,选择新建字符",False],
    ["界面操作/定义字符","在这里编辑字符的名字以供正则表达式引用",False],
# -----------------------------------------------------------
    ["界面操作/定义字符/搜索框","搜索框",True,SceneType.TEXT,"搜索框",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作/定义字符/搜索框","字符类型选择全路径或者列表",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/17customchar.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-440],
    ["界面操作/定义字符/搜索框","右侧的搜索框通过模糊搜索找到想要的类",False],
    ["界面操作/定义字符/搜索框","双击类名会展示类中的属性与函数",False],
    ["界面操作/定义字符/搜索框","点击这些项便可为字符设置具体的属性和函数",False],
    ["界面操作/定义字符/搜索框","当右侧列表项过多时",False],
    ["界面操作/定义字符/搜索框","可以再次使用搜索框对已有项进行过滤",False],
    ["界面操作/定义字符/搜索框","最后点击OK完成新建字符",False],
# -----------------------------------------------------------
    ["界面操作/定义字符/类范围","类范围",True,SceneType.TEXT,"类范围",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作/定义字符/类范围","如果希望字符能表示某个类或者某些类的全部属性或全部函数",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/18classscope.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-120],
    ["界面操作/定义字符/类范围","需要先在这个列表中添加类范围",False],
    ["界面操作/定义字符/类范围","与字符相同,类范围可以通过指定具体的类生成",False],
    ["界面操作/定义字符/类范围","也可以通过规则生成",False],
    ["界面操作/定义字符/类范围","同样是右键列表,选择新建类范围",False],
    ["界面操作/定义字符/类范围","在这里编辑类范围的名字,以供字符的生成规则使用",False],
    ["界面操作/定义字符/类范围","类范围类型同样有全路径和列表用于指定具体的类",False],
    ["界面操作/定义字符/类范围","其他类型请自行探索",False],
    ["界面操作/定义字符/类范围","从右侧列表选出想要的类后",False],
    ["界面操作/定义字符/类范围","点击OK完成新建类范围",False],
    ["界面操作/定义字符/类范围","回到字符列表,新建字符,编辑名字,选择类型为属性",False],
    ["界面操作/定义字符/类范围","点击刚新建的类范围,最后点击OK完成新建字符",False],
    ["界面操作/定义字符/类范围","此时这个字符代表了上面类范围中的所有属性",False],
    ["界面操作/定义字符/类范围","其他的字符类型请自行探索",False],
# -----------------------------------------------------------
    ["界面操作/编写正则/内置字符","内置字符",True,SceneType.TEXT,"内置字符",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作/编写正则/内置字符","将属性定义为字符后,就可以编写正则来搜索数据流动了",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/19buildinchar.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-170],
    ["界面操作/编写正则/内置字符","右键新建正则并编写名字,此时会显示非常多的按钮",False],
    ["界面操作/编写正则/内置字符","这些按钮用于添加内置字符",False],
    ["界面操作/编写正则/内置字符","这些内置字符中的大部分在自定义字符类型中出现过",False],
    ["界面操作/编写正则/内置字符","但与自定义字符不同的是,内置字符匹配的是对应类型的所有节点",False],
    ["界面操作/编写正则/内置字符","比如内置字符属性匹配所有类的所有属性",False],
    ["界面操作/编写正则/内置字符","而自定义字符类型属性,只匹配用户指定的类中的属性",False],
    ["界面操作/编写正则/内置字符","内置字符有极大的必要性",False],
    ["界面操作/编写正则/内置字符","因为用户需要依靠矢山来搜索数据的流向",False],
    ["界面操作/编写正则/内置字符","所以矢山不能要求用户",False],
    ["界面操作/编写正则/内置字符","提前把数据流动中涉及到的所有变量都设置为自定义字符",False],
    ["界面操作/编写正则/内置字符","正因有了内置字符",False],
    ["界面操作/编写正则/内置字符","用户可以只将他关心的变量设置为自定义字符",False],
    ["界面操作/编写正则/内置字符","添加完内置字符后",False],
    ["界面操作/编写正则/内置字符","将刚定义好的字符放置在开头",False],
    ["界面操作/编写正则/内置字符","点击OK完成正则的编写",False],
# -----------------------------------------------------------
    ["界面操作/编写正则/正则限制","正则限制",True,SceneType.TEXT,"正则限制",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作/编写正则/正则限制","注意",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/20regexconstraint.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-170],
    ["界面操作/编写正则/正则限制","一个有效的正则必须包含至少一个重复类型为一次的自定义字符",False],
    ["界面操作/编写正则/正则限制","从产品设计上来讲",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/chanpingjiaodu.jpeg",TransitionType.FADE,Transform([1.918,1.918],[0,-284],0)],
    ["界面操作/编写正则/正则限制","如果正则中没有自定义的字符",False],
    ["界面操作/编写正则/正则限制","说明用户没有具体关心的变量",False],
    ["界面操作/编写正则/正则限制","而是想让矢山去搜索一种数据流动模式在项目中的应用",False],
    ["界面操作/编写正则/正则限制","这并非矢山的产品功能",False],
    ["界面操作/编写正则/正则限制","从搜索空间上来讲",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/search2.jpeg",TransitionType.FADE,Transform([1.918,1.918],[0,-284],0)],
    ["界面操作/编写正则/正则限制","从自定义的字符开始搜索",False],
    ["界面操作/编写正则/正则限制","搜索空间才是合理的",False],
    ["界面操作/编写正则/正则限制","否则矢山需要从所有的属性开始搜索",False],
    ["界面操作/编写正则/正则限制","一个项目如果有一百万个属性",False],
    ["界面操作/编写正则/正则限制","那么就有一百万个搜索起点",False],
    ["界面操作/编写正则/正则限制","搜索空间大到难以承受",False],
# -----------------------------------------------------------
    ["界面操作/编写正则/正则复用","正则复用",True,SceneType.TEXT,"正则复用",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作/编写正则/正则复用","自定义字符为正则减小了搜索空间,但也带来了局限性",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/21regexreuse.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-120],
    ["界面操作/编写正则/正则复用","当你要搜索另一个变量的数据流向时",False],
    ["界面操作/编写正则/正则复用","要么得重新编写一个一模一样的正则",False],
    ["界面操作/编写正则/正则复用","要么得替换掉原先正则中的自定义字符,很不方便",False],
    ["界面操作/编写正则/正则复用","因此矢山为正则提供了参数",False],
    ["界面操作/编写正则/正则复用","右键新建实例,点击自定义字符以替换参数",False],
    ["界面操作/编写正则/正则复用","点击OK完成新建实例",False],
    ["界面操作/编写正则/正则复用","参数为正则提供了一种复用手段",False],
    ["界面操作/编写正则/正则复用","正则的另一种复用手段是编写正则片段",False],
    ["界面操作/编写正则/正则复用","右键新建正则并编写名字,选择正则类型为片段",False],
    ["界面操作/编写正则/正则复用","片段的编写没有必须包含一个自定义字符的限制",False],
    ["界面操作/编写正则/正则复用","点击OK完成片段编写",False],
    ["界面操作/编写正则/正则复用","此片段可以用在正则的编写中,达到复用的目的",False],
# -----------------------------------------------------------
    ["界面操作/搜索","开始搜索",True,SceneType.TEXT,"开始搜索",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作/搜索","正则编写完成后, escape键退出正则编辑面板",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/22startsearching.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-170],
    ["界面操作/搜索","快捷键s打开正则选择菜单,选择刚编写的正则",False],
    ["界面操作/搜索","快捷键control + f开始搜索",False],
    ["界面操作/搜索","快捷键control + h自动上色",False],
    ["界面操作/搜索","快捷键control + a全部选择",False],
    ["界面操作/搜索","其他快捷键请按1自行探索",False],
# -----------------------------------------------------------
    ["界面操作/搜索/数据加载","数据加载",True,SceneType.TEXT,"数据加载",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["界面操作/搜索/数据加载","需要注意的是刚才的加载界面",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/loading.jpg",TransitionType.NONE,Transform([0.637,0.637],[0,0],0)],
    ["界面操作/搜索/数据加载","加载的就是解析源码步骤产生的数据",False],
    ["界面操作/搜索/数据加载","由于矢山不会去分析用户正则的意图",False],
    ["界面操作/搜索/数据加载","因此这开头的加载范围是偏大的",False],
    ["界面操作/搜索/数据加载","如果所选正则中所有自定义字符所代表的属性或函数为A",False],
    ["界面操作/搜索/数据加载","那么加载范围是使用了A的所有类",False],
    ["界面操作/搜索/数据加载","当你看到加载界面显示有几百个类需要加载",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/23loadtoomuch.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-170],
    ["界面操作/搜索/数据加载","而你的意图又不在这几百个类中",False],
    ["界面操作/搜索/数据加载","可以通过快捷键a选择类范围作为搜索开始时加载的类范围",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/24chooseclassscope.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-20],
    ["界面操作/搜索/数据加载","矢山不仅会这样在搜索开始时显式的加载数据",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/loading.jpg",TransitionType.NONE,Transform([0.637,0.637],[0,0],0)],
    ["界面操作/搜索/数据加载","在正则搜索的过程中,如果因函数调用搜到其他的类中",False],
    ["界面操作/搜索/数据加载","矢山会隐式的加载这个类的数据,自动完成,用户无感",False],
    ["界面操作/搜索/数据加载","因此当你看到矢山搜索了很长时间却没有新增节点",False],
    ["界面操作/搜索/数据加载","而内存在一直增加",False],
    ["界面操作/搜索/数据加载","那就是矢山正忙着隐式加载数据",False],
    ["界面操作/搜索/数据加载","此时请修改正则,减小搜索范围",False],
    ["界面操作/搜索/数据加载","或者快捷键G",False],
    ["界面操作/搜索/数据加载","将重复类型星号的含义变为最多重复10次",False],
    ["界面操作/搜索/数据加载","以减小搜索范围",False],
    ["界面操作/搜索/数据加载","矢山没有提供停止搜索的操作",False],
    ["界面操作/搜索/数据加载","搜索时长如超出忍耐,请重启应用以结束搜索",False],
# -----------------------------------------------------------
    ["内置字符LV","内置字符LV",True,SceneType.TEXT,"内置字符LV",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["内置字符LV","LV表示局部变量",False],
    ["内置字符LV","矢山除了会用连线表示变量的读写关系外",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/26lvwrittenhis1.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,300],0),-350],
    ["内置字符LV","还会用连线表示一个变量被读取时它的值来自于哪里",False],
    ["内置字符LV","也就是它上次被写是在哪里",False],
    ["内置字符LV/1","对于作用域嵌套作用域的代码来说",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/27lvwrittenhis2.mp4",TransitionType.FADE,Transform([0.8,0.8],[100,0],0),-50],
    ["内置字符LV/1","局部变量上次被写的地方",False],
    ["内置字符LV/1","来自于声明它的作用域和子作用域",False],
    ["内置字符LV/2","对于一个有循环作用域的代码来说",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/28lvwritenhis3.mp4",TransitionType.FADE,Transform([0.8,0.8],[100,0],0),-50],
    ["内置字符LV/2","上次被写的地方可能来自被读的地方之后",False],
# -----------------------------------------------------------
    ["内置字符condition","内置字符condition",True,SceneType.TEXT,"内置字符condition",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["内置字符condition","condition 表示时机",False],
    ["内置字符condition","具体的说",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/29condition.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-50],
    ["内置字符condition","就是一个变量的读写或者一个函数的调用或者一个条件语句",False],
    ["内置字符condition","发生在了哪个条件语句下",False],
    ["内置字符condition","condition可以指向condition,局部变量,属性,函数,参数,函数返回",False],
    ["内置字符condition","都表示时机",False],
    ["内置字符condition","condition被condition或者method所指时表示时机",False],
    ["内置字符condition","condition被其他节点所指时表示逻辑控制",False],
    ["内置字符condition/TR","如果在条件语句C下,一个变量A被读取并写入变量B",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/30tr1.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-90],
    ["内置字符condition/TR","那么会有两条线从C分别指向A和B",False],
    ["内置字符condition/TR","但此时已经有一条线从A指向了B",False],
    ["内置字符condition/TR","那么这两条表示时机的线就有一条多余了",False],
    ["内置字符condition/TR","此时快捷键control+r",False],
    ["内置字符condition/TR","矢山会用Transitive Reduction算法解决此问题",False],
    ["内置字符condition/TR","注意:如果A和B的数据流动形成了循环",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/31tr2.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-20],
    ["内置字符condition/TR","那么使用过Transitive Reduction算法后",False],
    ["内置字符condition/TR","这个循环会完全脱离和条件语句C的连接",False],
    ["内置字符condition/TR","这并非矢山本意,而是算法性质导致的",False],
# -----------------------------------------------------------
    ["内置字符reference","内置字符reference",True,SceneType.TEXT,"内置字符reference",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["内置字符reference","reference表示对象引用和类引用",False],
    ["内置字符reference","引用关系的图形化并不复杂",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/32reference.mp4",TransitionType.FADE,Transform([1,1],[250,0],0),-50,[[SceneType.IMG,"/home/ydd/Documents/shishan/resource/arrow.png",Transform([1.4,0.25],[-148,-50],-3.14),0.6,1]]],
    ["内置字符reference","但是为了让一条正则能搜到更多的信息",False],
    ["内置字符reference","矢山设计了引用方向和数据流动方向保持一致的方案",False],
    ["内置字符reference","即:如果被引用的函数返回值没有被读取或没有返回值",False],
    ["内置字符reference","那么引用方向是逆向的",False],
# -----------------------------------------------------------
    ["边读边搜","边读边搜",True,SceneType.TEXT,"边读边搜",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["边读边搜","搜索完成后,用户开始读图",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/newrequest.jpeg",TransitionType.FADE,Transform([1.875,1.875],[0,-32],0)],
    ["边读边搜","从发展的角度讲,因为读图",False],
    ["边读边搜","用户对源码有了新的认识,因此产生了新的搜索需求",False],
    ["边读边搜","这新的搜索需求大概率是基于原图的",False],
    ["边读边搜","因此矢山提供了两种基于原图的搜索",False],
    ["边读边搜","第一种是快捷键control+d",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/33readandsearch.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-120],
    ["边读边搜","将选中的节点保存为一个自定义字符",False],
    ["边读边搜","用于下一轮的搜索",False],
    ["边读边搜","此方法适用于对属性的二次搜索",False],
    ["边读边搜","第二种是快捷键alt+逗号或句号",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/34readandsearch2.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-100],
    ["边读边搜","选择一个没有参数的正则或者正则片段",False],
    ["边读边搜","矢山会以选中的节点为开始或结尾进行二次搜索,扩充原图",False],
    ["边读边搜","此方法适用于对参数和返回值的二次搜索",False],
# -----------------------------------------------------------
    ["读图操作","读图操作",True,SceneType.TEXT,"读图操作",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["读图操作","矢山图中的节点有选中与未选中两种状态",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/35readgraph1.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-100],
    ["读图操作","这两种状态以不同的透明度进行区分",False],
    ["读图操作","而且选中的节点上会有文字,表达节点的含义",False],
    ["读图操作","快捷键n+减号可以减小未选中节点的透明度",False],
    ["读图操作","方便用户将注意力集中到选中的节点上",False],
    ["读图操作","节点刚被搜出来的时候是没有颜色的",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/36readgraph2.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-120],
    ["读图操作","快捷键control+h自动上色",False],
    ["读图操作","黄色表示入度为0的点",False],
    ["读图操作","洋红色表示出度为0的点",False],
    ["读图操作","其他节点会以渐变方式设置颜色",False],
    ["读图操作","选中一个点后,可以通过快捷键逗号或句号",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/37readgraph3.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-120],
    ["读图操作","向上或者向下选中相邻的点",False],
    ["读图操作","快捷键shift+逗号或句号可以向上选到顶或向下选到底",False],
    ["读图操作","选中一些点后,右键其中一个点,可以开始流动动画",False],
    ["读图操作","shift+右键节点，可以开始反向流动动画",False],
    ["读图操作","快捷键c取消所有选中的点,同时结束所有的流动动画",False],
    ["读图操作","当节点被分组后",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/38readgraph4.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-150],
    ["读图操作","control+单击,可以选中节点所在组中的所有节点",False],
    ["读图操作","快捷键u编辑选择维度",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/39readgraph.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-80],
    ["读图操作","并将选择的维度绑定到数字5到9这5个数字上",False],
    ["读图操作","按住数字5到9其中一个,同时单击节点",False],
    ["读图操作","会以被单击节点为开始,按照对应的维度限制",False],
    ["读图操作","选择所有联通的节点",False],
    ["读图操作","如果同时按住4,会以被单击节点为结束,反方向的选择",False],
    ["读图操作","空格 + 加号或减号进行缩放",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/40readgraph6.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-20],
    ["读图操作","空格 + 方向键进行平移",False],
    ["读图操作","双击节点使节点居中",False],
    ["读图操作","其他的阅读方式请在快捷键列表中探索",False],
# -----------------------------------------------------------
    ["矢山常用正则搭配","矢山常用正则搭配",True,SceneType.TEXT,"矢山常用正则搭配",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["矢山常用正则搭配","我以自身经验猜测你对代码阅读的常见需求",False],
    ["矢山常用正则搭配","这个变量值从哪里来的?",True,SceneType.TEXT,"这个变量值从哪里来的?",TransitionType.FADE,Transform([1,1],[0,0],0)],
    ["矢山常用正则搭配","这个变量值到哪里去,或者说怎么用的?",True,SceneType.TEXT,"这个变量值到哪里去?",TransitionType.FADE,Transform([1,1],[0,0],0)],
    ["矢山常用正则搭配","这个函数是从哪里调过来的?",True,SceneType.TEXT,"这个函数是从哪里调过来的?",TransitionType.FADE,Transform([1,1],[0,0],0)],
    ["矢山常用正则搭配","函数A是否调用了函数B?",True,SceneType.TEXT,"函数A是否调用了函数B?",TransitionType.FADE,Transform([1,1],[0,0],0)],
    ["矢山常用正则搭配","函数A触发函数B，需要什么条件?",True,SceneType.TEXT,"A触发B，需要什么条件?",TransitionType.FADE,Transform([1,1],[0,0],0)],
    ["矢山常用正则搭配","根据这些需求,矢山预先写好了很多正则与正则片段",True,SceneType.VIDEO,"/home/ydd/Documents/shishan/vid/25preparedregex.mp4",TransitionType.FADE,Transform([0.637,0.637],[0,0],0),-40],
    ["矢山常用正则搭配","方便用户参考和使用",False],
# -----------------------------------------------------------
    ["结束语","矢山的教程到此结束",True,SceneType.TEXT,"矢山的教程到此结束",TransitionType.NONE,Transform([1,1],[0,0],0)],
    ["结束语","人工智能来势汹汹,你我在角落瑟瑟发抖",True,SceneType.IMG,"/home/ydd/Documents/shishan/img/aiisgreat.jpeg",TransitionType.FADE,Transform([1.875,1.875],[0,-100],0)],
    ["结束语","希望矢山能以图形的方式",False],
    ["结束语","让你我理解代码的速度赶上人工智能编写代码的速度",False],
]




audio_dir = "/home/ydd/Documents/shishan/mp3/"

def clear_strips_in_channel(channel):
    sequencer = bpy.context.scene.sequence_editor
    if sequencer:
        for strip in sequencer.sequences:
            if strip.channel == channel:
                sequencer.sequences.remove(strip)

def addAudioStrip(channel,start_frame,mp3_file):
    audio_strip = bpy.context.scene.sequence_editor.sequences.new_sound(name=mp3_file, filepath=os.path.join(audio_dir, mp3_file),  channel=channel, frame_start=start_frame)
    return audio_strip

def addVideoStrip(channel,audio_strip,mp4_path,offset):
    video_strip = bpy.context.scene.sequence_editor.sequences.new_movie(name=mp4_path, filepath=mp4_path,  channel=channel, frame_start=audio_strip.frame_final_start + offset,fit_method='FIT')
    video_strip.frame_final_duration = audio_strip.frame_final_duration - offset
    video_strip.frame_offset_start = -offset
    video_strip.channel = channel
    return video_strip

def addImageScene(channel,audio_strip,image_path):
    image_strip = bpy.context.scene.sequence_editor.sequences.new_image(name=image_path, filepath=image_path, channel=channel, frame_start=audio_strip.frame_final_start)
    image_strip.frame_final_duration = audio_strip.frame_final_duration
    image_strip.blend_type = 'ALPHA_OVER'
    return image_strip

def addTextStrip(channel,audio_strip,text):
    # Create a text strip
    text_strip = bpy.context.scene.sequence_editor.sequences.new_effect(name=text, type='TEXT', channel=channel, frame_start=audio_strip.frame_final_start, frame_end=audio_strip.frame_final_end)
    # Set the text content
    text_strip.text = text
    text_strip.font_size = 120
    return text_strip

def addColorStrip(channel,audio_strip):
    color_strip = bpy.context.scene.sequence_editor.sequences.new_effect(name="Color", type='COLOR', channel=channel, frame_start=audio_strip.frame_final_start, frame_end=audio_strip.frame_final_end)
    color_strip.color = (0,0,0)
    return color_strip

def addSubTitle(channel,audio_strip,text):
    # Create a text strip
    text_strip = bpy.context.scene.sequence_editor.sequences.new_effect(name=text, type='TEXT', channel=channel, frame_start=audio_strip.frame_final_start, frame_end=audio_strip.frame_final_end)

    # Set the text content
    text_strip.text = text
    text_strip.font_size = 40 
    text_strip.use_box = True
    text_strip.box_color = (0, 0, 0, 0.7)
    text_strip.transform.offset_y=-480
    return text_strip


def applyTransform(strip,transform):
    strip.transform.scale_x = transform.scale[0]
    strip.transform.scale_y = transform.scale[1]
    strip.transform.offset_x = transform.position[0]
    strip.transform.offset_y = transform.position[1]
    strip.transform.rotation = transform.rotation

def addVisualStrip(audio_strip,script):
    channel = channel_visual1 if use_first_visual_strip else channel_visual2
    strip = None
    if (script[3] == SceneType.IMG):
        strip = addImageScene(channel,audio_strip,script[4])
    if (script[3] == SceneType.TEXT):
        strip = addTextStrip(channel,audio_strip,script[4])
    if (script[3] == SceneType.VIDEO):
        strip = addVideoStrip(channel,audio_strip,script[4],script[7])

    if (script[5] == TransitionType.FADE):
        strip.frame_final_start = strip.frame_final_start - 10
        bpy.context.scene.sequence_editor.sequences.new_effect("Cross", 'CROSS', channel_transition,frame_start=strip.frame_final_start-10, frame_end=strip.frame_final_start, seq1=last_visual_strip,seq2=strip)
    elif (script[5] == TransitionType.WIPE):
        strip.frame_final_start = strip.frame_final_start - 15
        eff_strip = bpy.context.scene.sequence_editor.sequences.new_effect("Wipe", 'WIPE', channel_transition,frame_start=strip.frame_final_start-15, frame_end=strip.frame_final_start, seq1=last_visual_strip,seq2=strip)
        eff_strip.transition_type = 'DOUBLE'
    applyTransform(strip,script[6])
    return strip

def addOverlayStrip(last_overlay_data,channel_i):
    channel = channel_overlay1
    strip = None
    if (last_overlay_data[0] == SceneType.IMG):
        strip = addImageScene(channel,last_visual_strip,last_overlay_data[1])
    if (last_overlay_data[0] == SceneType.COLOR):
        strip = addColorStrip(channel,last_visual_strip)
    if (last_overlay_data[0] == SceneType.TEXT):
        strip = addTextStrip(channel,last_visual_strip,last_overlay_data[1])
        strip.color = (1,0,0,1)
        strip.font_size = 57
    
    strip.frame_start = strip.frame_start + int(strip.frame_final_duration * last_overlay_data[3])
    strip.frame_final_duration = int(strip.frame_final_duration * (last_overlay_data[4] - last_overlay_data[3]))
    applyTransform(strip,last_overlay_data[2])
    return strip

channel_audio = 1
channel_visual1 = 3
channel_visual2 = 4
channel_transition = 5
channel_overlay1 = 6
channel_overlay2 = 7
channel_overlay3 = 8
channel_overlay4 = 9
channel_overlay5 = 10
channel_overlay6 = 11
channel_overlay7 = 12
channel_subtitle = 16
# Clear all strips in the specified channel
clear_strips_in_channel(1)
clear_strips_in_channel(2)
clear_strips_in_channel(3)
clear_strips_in_channel(4)
clear_strips_in_channel(5)
clear_strips_in_channel(6)
clear_strips_in_channel(7)
clear_strips_in_channel(8)
clear_strips_in_channel(9)
clear_strips_in_channel(10)
clear_strips_in_channel(11)
clear_strips_in_channel(12)
clear_strips_in_channel(13)
clear_strips_in_channel(14)
clear_strips_in_channel(15)
clear_strips_in_channel(16)

start_frame = 1
last_visual_strip = None
last_overlays_data = []
use_first_visual_strip = True
for i,script in enumerate(scriptObj):
    mp3_file = textToMp3FileName(script[1],i)
    audio_strip = addAudioStrip(channel_audio,start_frame,mp3_file)
    addSubTitle(channel_subtitle,audio_strip,script[1])
    if (script[2]):
        for i, last_overlay_data in enumerate(last_overlays_data):
            addOverlayStrip(last_overlay_data,i)
        last_visual_strip = addVisualStrip(audio_strip,script)
        use_first_visual_strip = not use_first_visual_strip
        last_overlays_data.clear()
        if (len(script)>8):
            last_overlays_data = script[8]
    else:
        if not last_visual_strip is None:
            last_visual_strip.frame_final_duration = last_visual_strip.frame_final_duration + audio_strip.frame_final_duration
    start_frame += audio_strip.frame_final_duration

for i, last_overlay_data in enumerate(last_overlays_data):
    addOverlayStrip(last_overlay_data,i)

bpy.context.scene.frame_end = start_frame