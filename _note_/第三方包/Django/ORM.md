查询单个列的值
story.object.values_list("url", flat=True)
SELECT `story`.`url` FROM `hbtc_story` WHERE `story`.`status` = resolved 

AND查询
Stories.objects.filter(Q(status='resolved') & Q(status='developing'))
SELECT * FROM `story` WHERE (`story`.`status` = resolved AND `story`.`status` = developing)

或查询
Stories.objects.filter(Q(status='resolved') | Q(status='developing'))
SELECT * FROM `story` WHERE (`story`.`status` = resolved OR `story`.`status` = developing)

NOT查询
Stories.objects.filter(~Q(status='resolved'))
SELECT * FROM `story` WHERE NOT (`story`.`status` = resolved)

查询为空
Stories.objects.filter(status__isnull=True)
SELECT  *  FROM `story` WHERE `story`.`plan_id_id` IS NULL

like查询
Stories.objects.filter(status__contains='resolved')
SELECT *  FROM `story` WHERE `story`.`status` LIKE BINARY %resolved%;
Stories.objects.filter(status__endswith='resolved')
SELECT *  FROM `story` WHERE `story`.`status` LIKE BINARY %resolved;
Stories.objects.filter(status__istartswith='resolved')
SELECT *  FROM `story` WHERE `story`.`status` LIKE BINARY resolved%;

in查询
Stories.objects.filter(status__in=('resolved',))
SELECT  *  FROM `story` WHERE `story`.`status` IN (resolved) ;

distinct查询
story.object.values_list("status", flat=True).distinct()
SELECT DISTINCT `story`.`status` FROM `story`