// Given a list of logs with IP addresses in the following format.
// lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]
//
// Return the most frequent IP address from the logs. The retuned IP address value must be in a string format.
//  If multiple IP addresses have the count equal to max count,
//  then return the address as a comma-separated string with IP addresses in sorted order.


// "static void main" must be defined in a public class.
public class Main {
    public static void main(String[] args) {
        System.out.println("Most Frequent IP!");

        getMostFrequentIp(new String[]{"10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20", "10.0.0.3 - GET 2020-08-24","10.0.0.3 - GET 2020-08-24","10.0.0.3 - GET 2020-08-24","10.0.0.4 - GET 2020-08-24",});
    }

    public static void getMostFrequentIp(String[] logs){
        HashMap<String, Integer> map = new HashMap<>();

        for(String log : logs){
            String[] arr = log.split(" ");
            map.put(arr[0], map.getOrDefault(arr[0], 0) + 1);
        }

        List<String> mostFrequent = new ArrayList<>();
        int freq = 0;

        for(String ip : map.keySet()){
            freq = Math.max(freq, map.get(ip));
        }

        for(String ip : map.keySet()){
            if(map.get(ip) == freq) mostFrequent.add(ip);
        }

        System.out.println(mostFrequent);
    }

}

