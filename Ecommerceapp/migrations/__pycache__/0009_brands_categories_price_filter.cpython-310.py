o
    ��dS  �                   @   s&   d dl mZmZ G dd� dej�ZdS )�    )�
migrations�modelsc                   @   s�   e Zd ZdgZejddejddddd�fdejd	d
�fgd�ejddejddddd�fdejd	d
�fgd�ejddejddddd�fdejg d�d	d�fgd�gZ	dS )�	Migration)�Ecommerceapp�0008_orders_orderupdate�Brands�idTF�ID)�auto_created�primary_key�	serialize�verbose_name�
Brand_name�d   )�
max_length)�name�fields�
Categories�Category�Price_Filter�price))�
100 TO 300r   )�
300 TO 500r   )�
500 TO 700r   )�
700 TO 900r   )�900 TO 1200r   )�1200 TO 1500r   )�1500 +r   )�choicesr   N)
�__name__�
__module__�__qualname__�dependenciesr   �CreateModelr   �BigAutoField�	CharField�
operations� r'   r'   �sC:\Users\sadgu\OneDrive\Desktop\Sippit-Folder\Sippit\Ecommerceapp\migrations\0009_brands_categories_price_filter.pyr      s,    ��������r   N)�	django.dbr   r   r   r'   r'   r'   r(   �<module>   s   