o
    ���c   �                   @   s&   d dl mZmZ G dd� dej�ZdS )�    )�
migrations�modelsc                   @   sF  e Zd ZdgZejddejddd�fdejdd	�fd
ej	dd�fdejdd	�fdejdd	�fdejdd	�fdejdd	�fdejdd	�fdejdd	�fdejdd	�fdejddd�fdejdddd�fdejddd�fdejd dd!�fgd"�ejd#d$ejddd�fdej	d d�fd%ejdd	�fd&ej
dd�fd'ejdd(�fgd"�gZd)S )*�	Migration)�EcommerceappZ0007_products�Orders�order_idTF)�primary_key�	serialize�
items_jsoni�  )�
max_length�amountr   )�default�name�Z   �email�address1��   �address2�city�d   �state�zip_code�oid�   )�blankr   �
amountpaidi�  )r   r   �null�paymentstatus�   �phone� )r   r   )r   �fields�OrderUpdate�	update_id�update_desc�	delivered�	timestamp)�auto_now_addN)�__name__�
__module__�__qualname__�dependenciesr   �CreateModelr   �	AutoField�	CharField�IntegerField�BooleanField�	DateField�
operations� r3   r3   �gC:\Users\sadgu\OneDrive\Desktop\Sippit-Folder\Sippit\Ecommerceapp\migrations\0008_orders_orderupdate.pyr      s>    ������r   N)�	django.dbr   r   r   r3   r3   r3   r4   �<module>   s   