
mapping_map = {
    "host"    : "192.168.1.222"       , # 控制器地址ip
    "multiAxis_EMERGENCYSTOP_data" : [12999,255]  ,
    "multiAxis_OriginAll_data" : [12997,255]  ,
    "num_ch" : 4 ,          # 通道数
    
    "mapping" : {
        # 各功能操作的起始地址的参数映射字典
        # 操作数 : {“功能名”：[每轴x个寄存器;   读取的寄存器的基地址;   写入的寄存器的基地址;   单双字;  0:只读 1:只写 2:读写]}
        "data_map": {
            1         :  {"multiAxisStateRead"         : [6, 12000,  None, 2, 0]},     # 读保持寄存器状态
            2         :  {"multiAxisStop"              : [2,  None, 12096, 2, 1]},     # 停止
            3         :  {"multiAxisRelativeMove"      : [2,  None, 12128, 2, 1]},     # 相对移动 
            4         :  {"multiAxisAbsoluteMove"      : [2, 12160, 12160, 2, 2]},     # 绝对移动
            5         :  {"multiAxisRelativeSpeedMove" : [4,  None, 12552, 2, 1]},     # 相对移动 + 指定速度
            6         :  {"multiAxisAbsoluteSpeedMove" : [4,  None, 12616, 2, 1]},     # 绝对移动 + 指定速度
            7         :  {"multiAxisHoming"            : [2,  None, 12680, 2, 1]},     # 回零点 
        },
        # 各通道状态读取的起始地址
        # 通道名 ： [“通道”，当前速度的地址，单双字，微分细步地址，当前位置的地址]
        "read_map" : {
            "ch0" : ['X_1', 10120,2,10150,10102],
            "ch1" : ['X_2', 10220,2,10250,10202],
            "ch2" : [' Y ', 10320,2,10350,10302],
            "ch3" : [' Z ', 10420,2,10450.10402]
        }
    }
}