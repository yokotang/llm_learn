import qrcode
import io

def maker_qrcode(url,save_path=None):
    """
    生成二维码
    :param url: 需要生成二维码的url
    :return: 返回图片字节流
    """
    image = qrcode.make(url)  # 创建二维码片
    if save_path:
        image.save(save_path)
        print(f"二维码已保存到: {save_path}")

    buffer = io.BytesIO()
    # 将图片内容丢入容器
    image.save(buffer, 'png')
    # 返回容器内的字节
    return buffer.getvalue()
baidu=maker_qrcode("https://www.upsort.com/",save_path="upsort.png")
print(baidu)