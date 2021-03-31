```javascript
	function confirm_delete(){
	layer.open({
	title:"确认删除",
	content:"确认删除这篇文章吗？",
	yes:function(index,layero){
	location.href='{% url:'blog:article_delete' article.id %}'
	}
	})
	}