o
    ��c�  �                   @   s&   d dl mZmZ G dd� dej�ZdS )�    )�
migrations�modelsc                
   @   sp   e Zd ZdZg Zejddejddddd�fdej	dd	�fd
ej
dd	�fdej	dd	�fdejdd	�fgd�gZdS )�	MigrationT�Contact�idF�ID)�auto_created�primary_key�	serialize�verbose_name�name�2   )�
max_length�email��   �desci�  �phonenumberi�  )r   �fieldsN)�__name__�
__module__�__qualname__�initial�dependenciesr   �CreateModelr   �BigAutoField�	CharField�
EmailField�	TextField�
operations� r   r   �\C:\Users\sadgu\OneDrive\Desktop\Sippit-Folder\Sippit\Ecommerceapp\migrations\0001_initial.pyr      s    ���r   N)�	django.dbr   r   r   r   r   r   r    �<module>   s   