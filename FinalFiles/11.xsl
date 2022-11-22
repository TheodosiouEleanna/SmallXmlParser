<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="@* | node()">
      <html>
         <head>
            <link rel="stylesheet" type="text/css" href="style.css" />
         </head>
         <body>
            <h2>Schedule</h2>
            <style></style>
            <table border="1">
               <tr bgcolor="">
                  <th>Title</th>
                  <th>Professor</th>
                  <th>Day</th>
               </tr>
               <xsl:for-each select="/Schedule/Lesson">
                  <xsl:sort select="Lecture/Day/@class" />

                  <tr>
                     <xsl:choose>
                        <xsl:when test="Day = 'Monday'">
                           <td>
                              <xsl:value-of select="Title" />
                           </td>
                           <td>
                              <xsl:value-of select="Professor" />
                           </td>
                           <td bgcolor="ff0000">
                              <xsl:value-of select="Lecture/Day" />
                           </td>
                        </xsl:when>
                        <xsl:when test="Day = 'Wednesday'">
                           <td>
                              <xsl:value-of select="Title" />
                           </td>
                           <td>
                              <xsl:value-of select="Professor" />
                           </td>
                           <td>
                              <xsl:value-of select="Lecture/Day" />
                           </td>
                        </xsl:when>
                        <xsl:when test="Day = 'Thursday'">
                           <td>
                              <xsl:value-of select="Title" />
                           </td>
                           <td>
                              <xsl:value-of select="Professor" />
                           </td>
                           <td>
                              <xsl:value-of select="Lecture/Day" />
                           </td>
                        </xsl:when>
                        <xsl:when test="Day = 'Friday'">
                           <td>
                              <xsl:value-of select="Title" />
                           </td>
                           <td>
                              <xsl:value-of select="Professor" />
                           </td>
                           <td>
                              <xsl:value-of select="Lecture/Day" />
                           </td>
                        </xsl:when>
                        <xsl:otherwise></xsl:otherwise>
                     </xsl:choose>
                     <td>
                        <xsl:value-of select="Title" />
                     </td>
                     <td>
                        <xsl:value-of select="Professor" />
                     </td>
                     <td>
                        <xsl:value-of select="Lecture/Day" />
                     </td>
                  </tr>
               </xsl:for-each>
            </table>
         </body>
      </html>
   </xsl:template>

</xsl:stylesheet>