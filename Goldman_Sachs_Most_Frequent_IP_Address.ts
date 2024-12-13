// Given a list of logs with IP addresses in the following format.
// lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]
//
// Return the most frequent IP address from the logs. The retuned IP address value must be in a string format.
//  If multiple IP addresses have the count equal to max count,
//  then return the address as a comma-separated string with IP addresses in sorted order.


function frequentIP(addresses: string[]): string {
    let maxCount = 0;
    const table: Record<string, number> = {};

    for (const addr of addresses) {
        const ip = addr.split(" ")[0];
        table[ip] = (table[ip] || 0) + 1;
        maxCount = Math.max(maxCount, table[ip]);
    }

    const maxIps: string[] = Object.entries(table)
        .filter(([_, count]) => count === maxCount)
        .map(([ip]) => ip);

    if (maxIps.length > 1) {
        return maxIps.sort().join(",");
    } else {
        return maxIps[0];
    }
}

// Test case
const lines: string[] = [
    "10.0.0.1 - GET 2020-08-24",
    "10.0.0.1 - GET 2020-08-24",
    "10.0.0.2 - GET 2020-08-20",
];

console.log(frequentIP(lines)); // Output: "10.0.0.1"
