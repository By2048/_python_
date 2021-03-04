from enum import Enum


class Code(Enum):
    # Api接口通用返回
    success = (0, '处理成功')
    no_result = (1, "没有相关数据")
    unknown_error = (2, '未知错误')

    def to_json(self, data=None):
        if self.value[0] == 0:
            result = {'code': self.value[0]}
            if data:
                result['data'] = data
            else:
                result['message'] = self.value[1]
        else:
            result = {'code': self.value[0], 'message': self.value[1]}
        return result


if __name__ == '__main__':
    assert Code.success.to_json() == {'code': 0, 'message': '处理成功'}
    assert Code.success.to_json(data=[1, 2, 3]) == {'code': 0, 'data': [1, 2, 3]}
    assert Code.no_result.to_json() == {'code': 1, 'message': '没有相关数据'}
