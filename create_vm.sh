#!/bin/bash
#

echo "Start test:"
#создание виртальной машины 


sudo virt-install \
  --virt-type=kvm \
  --name $1 \
  --memory 1024 \
  --vcpus 1 \
  --os-variant=rhel7\
  --hvm \
  --cdrom $2\
  --network network=default,model=virtio \
  --graphics vnc,port=$3\
  --disk path=/var/lib/libvirt/images/$1.img,size=8,bus=virtio\
  --noautoconsole

