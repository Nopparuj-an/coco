#
# Regular cron jobs for the coco package
#
0 4	* * *	root	[ -x /usr/bin/coco_maintenance ] && /usr/bin/coco_maintenance
