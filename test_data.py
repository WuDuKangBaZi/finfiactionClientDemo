from Model import order, inbounds, user_model, invoice
from Model.invoice import insert_invoice
from Model.user_model import insert_user


def run_test():
    invoice_data = [
        ['吉林省金康安医药有限责任公司', '山东及时雨汽车科技有限公司', '24372000000035547856', '17.90', '17.38', '0.52',
         "电子发票(普通发票)"],
        ['吉林省金康安医药有限责任公司', '郑州兴隆石化有限公司', '24412000000035099450', '373.00', '330.09', '42.91',
         '电子发票(普通发票)'],
        ['吉林省金康安医药有限责任公司', '郑州市管城回族区沙胆彪餐饮店', '24412000000017490386', '2150.00', '2128.71',
         '21.29', '电子发票(普通发票)'],
        ['吉林省金康安医药有限责任公司', '鼓楼区好望角广告装饰部', '24412000000031715887', '1110.00', '1099.01',
         '10.99', '电子发票(普通发票)'],
        ['吉林省金康安医药有限责任公司', '郑州市管城回族区康莱餐饮店(个体工商户)', '24412000000018411621', '1180.84',
         '1169.15', '11.69', '电子发票(普通发票)'],
        ['吉林省金康安医药有限责任公司', '永康市一丫工贸有限公司', '24332000000079499546', '1330.00', '1316.83',
         '13.17', '电子发票(普通发票)'],
        ['吉林省金康安医药有限责任公司', '郑州市管城回族区沙胆彪餐饮店', '24412000000025438409', '1435.00', '1420.79',
         '14.21', '电子发票(普通发票)'],
        ['吉林省金康安医药有限责任公司', '郑州昀之轩餐饮管理有限公司', '24412000000026222808', '138.00', '136.63',
         '1.37', '电子发票(普通发票)'],
        ['吉林省金康安医药有限责任公司', '郑州市金水区友晋餐饮店(个体工商户)', '24412000000033843533', '205.90',
         '203.86', '2.04', '电子发票(普通发票)'],
        ['吉林省金康安医药有限责任公司', '郑州梦想天空有限公司', '24412000000033846736', '167.19', '165.12', '2.07',
         '增值税专用发票'],
        ['河南省凯塞木业有限责任公司', '杭州市戈雅酒店', '24412000000032646732', '248.00', '240.68', '7.62',
         '增值税专用发票'],
        ['合肥市姚蔡制药有限责任公司', '永康市一丫工贸有限公司', '24412000000039846767', '368.26', '355.17', '12.99',
         '增值税专用发票']]
    invoice.create_table()
    for item in invoice_data:
        insert_invoice(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    # ["商品名称","规格","单位(售方名称)","数量","单价","金额","订单编号"],
    order_data = [
              ['通勤费', '6', '山东及时雨汽车科技有限公司', '3', '5.96', '17.90', '24372000000035547856'],
              ['汽油', '4', '郑州兴隆石化有限公司', '5', '74.6', '373.00', '24412000000035099450'],
              ['餐饮费用', '8', '郑州市管城回族区沙胆彪餐饮店', '2', '2150.00', '2128.71', '24412000000017490386'],
              ['窗帘*5', '3', '鼓楼区好望角广告装饰部', '5', '222.0', '1110.00', '24412000000031715887'],
              ['餐饮费', '9', '郑州市管城回族区康莱餐饮店(个体工商户)', '5', '236.16', '1180.84', '24412000000018411621'],
              ['摸高器*5', '1', '永康市一丫工贸有限公司', '5', '266.0', '1330.00', '24332000000079499546'],
              ['餐饮费', '7', '郑州市管城回族区沙胆彪餐饮店', '1', '1435.0', '1435.00', '24412000000025438409'],
              ['餐饮费', '3', '郑州昀之轩餐饮管理有限公司', '5', '27.6', '138.00', '24412000000026222808'],
              ['餐饮费', '8', '郑州市金水区友晋餐饮店(个体工商户)', '4', '205.90', '203.86', '24412000000033843533'],
              ['餐饮费', '5', '郑州梦想天空有限公司', '2', '83.595', '167.19', '24412000000033846736'],
              ['住宿费', '6', '杭州市戈雅酒店', '1', '248.0', '248.00', '24412000000032646732'],
              ['哑铃*5', '2', '永康市一丫工贸有限公司', '5', '73.652', '368.26', '24412000000039846767']]
    order.create_table()
    for item in order_data:
        order.insert(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        #["公司名称","供应商名称","单据编号(随机生成)","业务日期","物料名称","数量","价税合计","关联id"],
    warehouse_data = [
              ['吉林省金康安医药有限责任公司', '山东及时雨汽车科技有限公司', '388', '2024-1-7', '通勤费', '3', '17.90', '24372000000035547856'],
              ['吉林省金康安医药有限责任公司', '郑州兴隆石化有限公司', '132', '2024-1-19', '通勤费', '3', '373.00', '24412000000035099450'],
              ['吉林省金康安医药有限责任公司', '郑州市管城回族区沙胆彪餐饮店', '356', '2024-4-8', '通勤费', '3', '2150.00', '24412000000017490386'],
              ['吉林省金康安医药有限责任公司', '鼓楼区好望角广告装饰部', '947', '2024-1-4', '通勤费', '3', '1110.00', '24412000000031715887'],
              ['吉林省金康安医药有限责任公司', '郑州市管城回族区康莱餐饮店(个体工商户)', '323', '2024-1-6', '通勤费', '3', '1180.84', '24412000000018411621'],
              ['吉林省金康安医药有限责任公司', '永康市一丫工贸有限公司', '304', '2024-1-14', '通勤费', '3', '1330.00', '24332000000079499546'],
              ['吉林省金康安医药有限责任公司', '郑州市管城回族区沙胆彪餐饮店', '957', '2024-4-12', '通勤费', '3', '1435.00', '24412000000025438409'],
              ['吉林省金康安医药有限责任公司', '郑州昀之轩餐饮管理有限公司', '762', '2024-3-8', '通勤费', '3', '138.00', '24412000000026222808'],
              ['吉林省金康安医药有限责任公司', '郑州市金水区友晋餐饮店(个体工商户)', '690', '2024-3-2', '通勤费', '3', '205.90', '24412000000033843533'],
              ['吉林省金康安医药有限责任公司', '郑州梦想天空有限公司', '510', '2024-4-5', '通勤费', '3', '167.19', '24412000000033846736'],
              ['河南省凯塞木业有限责任公司', '杭州市戈雅酒店', '141', '2024-1-25', '通勤费', '3', '248.00', '24412000000032646732'],
              ['合肥市姚蔡制药有限责任公司', '永康市一丫工贸有限公司', '728', '2024-3-8', '通勤费', '3', '368.26', '24412000000039846767']]
    warehousing.create_table()
    for item in warehouse_data:
        warehousing.insert(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
    user_info = [
        ['财务管理员', 'admin', '123456'],
        ['普通员工', 'user1', '123456'],
        ['库房', 'user2', '123456'],
]
    user_model.create_table()
    for item in user_info:

        insert_user(item[0], item[1], item[2])