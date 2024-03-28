import json

controller_axis_mapping = {}                                              # 控制器每个输出通道的每个功能的起始地址的参数映射字典

with open('src/ros_modbus_msg/mapping.json', 'r') as f:
    data = json.load(f)


host =  data['host']                                                      # 控制器地址ip
multiAxis_EMERGENCYSTOP_data = data['multiAxis_EMERGENCYSTOP_data']        
multiAxis_OriginAll_data = data['multiAxis_OriginAll_data']
num_ch = data['num_ch']                                                   # 通道数

mapping = data['mapping']

# 各功能操作的起始地址的参数映射字典
# 操作数 : {“功能名”：[每轴x个寄存器;   读取的寄存器的基地址;   写入的寄存器的基地址;   单双字;  0:只读 1:只写 2:读写]}
data_map = mapping['data_map']

# 各通道状态读取的起始地址
# 通道名 ： [“通道”，当前速度的地址，单双字，微分细步地址，当前位置的地址]                                      
read_map = mapping['read_map']


# 计算公式
def address_calculate_formula(key, num_ch):
    """
    每通道的每个功能的起始地址的计算公式
    """
    data = data_map[key]
    if data[4] == 0:
        return data[1] + data[0] * num_ch
    elif data[4] == 1:
        return data[2] + data[0] * num_ch
    else:
        return data[1] + data[0] * num_ch


# 计算函数
def formula_result(num_ch):
    """
    通过date_map和address_caluculate_formula 公式计算每个通道的每个功能的起始地址；
    """
    axis_map = {}
    for ch in range(num_ch):
        axis_map[ch] = {}
        for key in data_map:
            if key in data_map:
                k = address_calculate_formula(key, ch)
                axis_map[ch][key] = k
    for ch, values in axis_map.items():
        controller_axis_mapping[ch] = [values[key] for key in values]


# 读寄存器状态：生成读状态结果索引表
def StateRead_OperationTable(num_elements):
    StateRead_data = []
    for i in range(num_elements):
        # 生成每个操作的名称和索引
        operation_name = f"CH{i}"
        status_index = i * 6 + 1
        position_index = i * 6 + 3
        speed_index = i * 6 + 5
        
        # 创建操作字典并添加到列表中
        operation_data = {
            "name": operation_name,
            "status_index": status_index,
            "position_index": position_index,
            "speed_index": speed_index
        }
        StateRead_data.append(operation_data)

    return StateRead_data

