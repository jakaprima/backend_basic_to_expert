const { InfluxDB, Point } = require('@influxdata/influxdb-client');

// Replace with your InfluxDB details
const url = "http://localhost:8086";
const token = "Lma6AKx39JdgnetNwIrE3WzhPgpcFKlY2vZYuXdSuhGjp6oTlNaRiNqy2TidGMPNGwKoXtYMxeIDS_zA5OmJTA==";
const org = "itmentorapps";
const bucket = "bucket_name";

const client = new InfluxDB({url: 'http://localhost:8086', token: token})


// write data
// async function writeData(measurement, tags, fields) {
//     const writeApi = client.getWriteApi(org, bucket);
  
//     const point = new Point(measurement)
//       .tag(tags)
//       .floatField(fields.name, fields.value);
  
//     await writeApi.writePoint(point);
//   }
  
//   // Example usage
//   writeData("cpu_temperature", { host: "server01" }, { name: "value", value: 55.2 })
//     .then(() => console.log("Data written successfully!"))
//     .catch(err => console.error("Error writing data:", err));
  
async function readData() {
    const query = `from(bucket:"${bucket}") select *`;
    const result = await client.getQueryApi(org).queryRows(query, {
        next(row, tableMeta) {
          const o = tableMeta.toObject(row)
          console.log(
            `${o._time} ${o._measurement} in '${o.location}' (${o.example}): ${o._field}=${o._value}`
          )
        },
        error(error) {
          console.error(error)
          console.log('\\nFinished ERROR')
        },
        complete() {
          console.log('\\nFinished SUCCESS')
        },
      });
    
    // for (const row of result) {
    //     console.log(
    //     `Measurement: ${row.measurement}, Tags: ${JSON.stringify(
    //         row.tags
    //     )}, Fields: ${JSON.stringify(row.fields)}`
    //     );
    // }
    }
    
    readData()
    .then(() => console.log("Data read successfully!"))
    .catch(err => console.error("Error reading data:", err));
      
