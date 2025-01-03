<style>
th {
  vertical-align: middle;
  text-align: center;
  white-space:pre-line;
  word-break: break-all;
  
}

table {
    table-layout: fixed;
}

xmp {   
  white-space: pre-wrap;
  word-wrap: break-word;
}

td {
  vertical-align: middle;
  word-wrap:break-word;
  white-space:pre-line;
  border: 1px solid;
}
</style>

<table>
    <thead>
        <tr>
            <th>MANAGEMENT IP: <u>{{MANAGEMENT_IP}}</u> MODEL: <u>{{DEVICE_HARDWARE}}</u></th>
            <th>REGION</th>
            <th>COUNTRY</th>
            <th>SITE</th>
            <th><u>{{DEVICE_HARDWARE}}</u> has a serial of: <u>{{DEVICE_SERIAL}}</u></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{{DEVICE_HOSTNAME}}</td>
            <td>{{REGION}}</td>
            <td>{{COUNTRY}}</td>
            <td>{{SITE}}</td>
            <td style="color:#0000ff"; "word-wrap: break-word"><span style="font-weight:bold"><pre>{{SHOW_OR_CHANGE_OUTPUT}}</pre></span></td>
        </tr>
    </tbody>
</table>