
## API Reference

#### Auth payload

```
  /api/*
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**.  username |
| `password` | `string` | **Required**.  password |

#### Get all category

```
  GET /api/category/
```

#### Get category

```
  GET /api/category/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of category to fetch |


#### Category Add

```
  POST /api/category/
```

| Payload | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. category name |
| `image_url`      | `file` | **Required**. category image |


#### Category Update

```
  PUT /api/category/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. category id |

#### Category Delete

```
  DELETE /api/category/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. category id |



#### Get all subcategory

```
  GET /api/subcategory/
```

#### Get subcategory

```
  GET /api/subcategory/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of category to fetch |


#### Subcategory Add

```
  POST /api/subcategory/
```

| Payload | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. subcategory name |
| `category`      | `option` | **Required**. foreign key with category |


#### Subcategory Update

```
  PUT /api/category/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. subcategory id |

#### Subcategory Delete

```
  DELETE /api/subcategory/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. subcategory id |



#### Get all Persons

```
  GET /api/person/
```

#### Get person

```
  GET /api/person/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of person to fetch |


#### Person Add

```
  POST /api/perosn/
```

| Payload | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `category`      | `option` | **Required**. foreign key with category |
| `sub_category`      | `option` | **Required**. foreign key with subcategory |
| `name`      | `string` | **Required**. Name |
| `number`      | `string` | **Required**.  Number |
| `rank`      | `string` | **Required**. Rank |
| `address`      | `string` | **Required**. Adress |


#### Person Update

```
  PUT /api/person/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. person id |

#### Person Delete

```
  DELETE /api/person/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. person id |

#### Person Search

```
  POST /api/person/search/
```

| Payload | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `search`      | `any` | **Required**. Search keyword |
