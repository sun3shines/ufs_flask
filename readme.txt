unique && universal fs

所以，当下载文件的时候，则是产生一个app_iter 从md5层中返回了。

上传文件，首先是检测md5值是否存在。然后在执行真正的上传功能了，传入req.environ['wsgi.inpu']

urlexist 检测文件是否存在了。
urlput
urlget

urlhead
urlpost
上层的业务压迫下层的对象，要求下层的对象是确定的，这样两者一压迫，那么中间的组织形式就出来了。是的。

爬虫功能。是的。

写一个MD5的调度和访问算法。是的。 记录读写层次。

关键字是传入的MD5.读取，或者写入的时候，都对该MD5的key进行统计了。加锁访问。是的。需要好好的规划下了。是的。自动实现目的地的迁移。以及，返回正确的位置了

传递两次，第一次，只带有md5，和metadata，如果失败，则传递第二次了。验证空字符串(不可取，需要读出所有的数据了。)和md5是否相同了。返回失败，则传递第二次了。是的。需要传递MD5值和DataType:NULL

然后对内进行验证了。是的。验证md5值和原先的是否相同。如果相同，则成功，更新meta，否则失败。

第二次，则传递真实的数据了。重新判断一把了。

然后关于数据的相关操作，比如说put，get，head，post，都定位到此对象上了。是的。

分层思想，所有的对于path的处理，导入到对于底层的技术细节的处理了。是的。

算法的作用，是模块内优化了。与整体分析设计无关了。关键是模块化和层次化，优化可在模块内进行了。


