```py

# @csrf_exempt
def test_ajax(request):
    """
    用户评分图片
    """
    if request.method == 'GET':
        return render(request, 'home/test_ajax.html')

    if request.method == 'POST':
        # id = request.POST.get('id', 0)
        user = request.user

        logging.error(user)
        pp = user.sex1
        logging.error(pp)
        logging.error('stop')
        return JsonResponse({"success": "23sdr123====7879789"})


path('test_ajax/', test_ajax, name='test_ajax'),

```


```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <script src="{% static 'lib/jquery/jquery-3.3.1.min.js' %}"></script>
    <meta charset="UTF-8">
    <title>test_ajax</title>
    <script>
        $(document).ready(function () {
            {#var a = $("#pp").html();#}
            {#alert(a);#}

            $("#btn").click(function () {
                $.ajax({
                    url: "{% url 'home:test_ajax' %}",
                    type: "post",
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}',
                        info: JSON.stringify({"id": 'id_test'})
                    },
                    success: function (ret_json) {
                        alert(ret_json.success)
                    }
                })
            });
        });
    </script>
</head>
<body>

<p id="pp">rwerwe-----</p>
<button id="btn">--btn---</button>


</body>
</html>
```