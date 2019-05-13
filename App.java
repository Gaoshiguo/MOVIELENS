package recommendation.movie;

import org.apache.mahout.cf.taste.impl.common.LongPrimitiveIterator;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.NearestNUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.Recommender;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;

import java.io.File;
import java.util.Arrays;
import java.util.List;
import java.io.PrintStream;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileDescriptor;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * 推荐思路
 * 1、读取用户-物品-评分数据，转换成推荐数据模型
 * 2、基于用户相似度计算用户N-最近邻
 * 3、使用推荐引擎推荐物品
 */
public class App {
    public static void main(String[] args) {

        //用户-物品-评分数据文件
        String filePath = "E:\\u_v_training.txt";
        //数据模型
        DataModel dataModel = null;
        try {
            //文件数据转换成数据模型
            dataModel = new FileDataModel(new File(filePath));
            /**
             * 用户相似度定义
             */
            //余弦相似度
//          UserSimilarity userSimilarity= new UncenteredCosineSimilarity(dataModel);
            //欧几里得相似度
//          UserSimilarity userSimilarity= new EuclideanDistanceSimilarity(dataModel);
            //皮尔森相似度
            UserSimilarity userSimilarity = new PearsonCorrelationSimilarity(dataModel);

            //定义用户的2-最近邻
            UserNeighborhood userNeighborhood = new NearestNUserNeighborhood(2, userSimilarity, dataModel);
            //定义推荐引擎
            Recommender recommender = new GenericUserBasedRecommender(dataModel,userNeighborhood, userSimilarity);
            //从数据模型中获取所有用户ID迭代器
            LongPrimitiveIterator usersIterator = dataModel.getUserIDs();
            //通过迭代器遍历所有用户ID
            while (usersIterator.hasNext()) {
              System.out.println("================================================");
                //用户ID
                long userID = usersIterator.nextLong();
                //用户ID
                LongPrimitiveIterator otherusersIterator = dataModel.getUserIDs();
                //遍历用户ID，计算任何两个用户的相似度
                while (otherusersIterator.hasNext()) {
                    Long otherUserID = otherusersIterator.nextLong();
                    System.out.println("用户 " + userID + " 与用户 " + otherUserID + " 的相似度为："
                            + userSimilarity.userSimilarity(userID, otherUserID));
                }
                //userID的N-最近邻
                long[] userN = userNeighborhood.getUserNeighborhood(userID);
                //用户userID的推荐物品，最多推荐两个
                List<RecommendedItem> recommendedItems = recommender.recommend(userID, 10);
                System.out.println("用户 "+userID + " 的最相近的两个相邻用户是 "+ Arrays.toString(userN));
                System.out.println(recommendedItems);  
                if (recommendedItems.size() > 0) {
        
                    for (RecommendedItem item : recommendedItems) {
                        System.out.println("推荐的物品"+ item.getItemID()+"预测评分是 "+ item.getValue());                                         
                    }
                } else {
                    System.out.println("无任何物品推荐");
                }             
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}