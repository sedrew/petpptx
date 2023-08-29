.. _Chart:

Chart - Main Chart Object
=========================

Each chart is contained in its own part like `chart1.xml`.


`Chart.font`
------------

By default, a new chart appears with an 18-point font that is applied to its
axes, the legend, tick labels, etc. The size, color, etc. can be specified
for the chart as a whole by settings attributes on
`/c:chartSpace/c:txPr/a:p/a:pPr/a:defRPr`.

.. highlight:: xml


XML Specimens
-------------

Default `c:txPr` element::

  <c:chartSpace>
    <!-- ... -->
    <c:txPr>
      <a:bodyPr/>
      <a:lstStyle/>
      <a:p>
        <a:pPr>
          <a:defRPr sz="1800"/>
        </a:pPr>
        <a:endParaRPr lang="en-US/>  <!-- may be locale dependent -->
      </a:p>
    </c:txPr>
    <!-- ... -->
  </c:chartSpace>


Related Schema Definitions
--------------------------

.. highlight:: xml

::

  <!-- homonym <c:chart> element in graphicData element -->

  <xsd:element name="chart" type="CT_RelId"/>

  <xsd:complexType name="CT_RelId">
    <xsd:attribute ref="r:id" use="required"/>
  </xsd:complexType>


  <!-- elements in chartX.xml part -->

  <xsd:element name="chartSpace" type="CT_ChartSpace"/>

  <xsd:complexType name="CT_ChartSpace">
    <xsd:sequence>
      <xsd:element name="date1904"       type="CT_Boolean"           minOccurs="0"/>
      <xsd:element name="lang"           type="CT_TextLanguageID"    minOccurs="0"/>
      <xsd:element name="roundedCorners" type="CT_Boolean"           minOccurs="0"/>
      <xsd:element name="style"          type="CT_Style"             minOccurs="0"/>
      <xsd:element name="clrMapOvr"      type="a:CT_ColorMapping"    minOccurs="0"/>
      <xsd:element name="pivotSource"    type="CT_PivotSource"       minOccurs="0"/>
      <xsd:element name="protection"     type="CT_Protection"        minOccurs="0"/>
      <xsd:element name="chart"          type="CT_Chart"/>
      <xsd:element name="spPr"           type="a:CT_ShapeProperties" minOccurs="0"/>
      <xsd:element name="txPr"           type="a:CT_TextBody"        minOccurs="0"/>
      <xsd:element name="externalData"   type="CT_ExternalData"      minOccurs="0"/>
      <xsd:element name="printSettings"  type="CT_PrintSettings"     minOccurs="0"/>
      <xsd:element name="userShapes"     type="CT_RelId"             minOccurs="0"/>
      <xsd:element name="extLst"         type="CT_ExtensionList"     minOccurs="0"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="CT_Chart">
    <xsd:sequence>
      <xsd:element name="title"            type="CT_Title"         minOccurs="0"/>
      <xsd:element name="autoTitleDeleted" type="CT_Boolean"       minOccurs="0"/>
      <xsd:element name="pivotFmts"        type="CT_PivotFmts"     minOccurs="0"/>
      <xsd:element name="view3D"           type="CT_View3D"        minOccurs="0"/>
      <xsd:element name="floor"            type="CT_Surface"       minOccurs="0"/>
      <xsd:element name="sideWall"         type="CT_Surface"       minOccurs="0"/>
      <xsd:element name="backWall"         type="CT_Surface"       minOccurs="0"/>
      <xsd:element name="plotArea"         type="CT_PlotArea"/>
      <xsd:element name="legend"           type="CT_Legend"        minOccurs="0"/>
      <xsd:element name="plotVisOnly"      type="CT_Boolean"       minOccurs="0"/>
      <xsd:element name="dispBlanksAs"     type="CT_DispBlanksAs"  minOccurs="0"/>
      <xsd:element name="showDLblsOverMax" type="CT_Boolean"       minOccurs="0"/>
      <xsd:element name="extLst"           type="CT_ExtensionList" minOccurs="0"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="CT_Style">
    <xsd:attribute name="val" type="ST_Style" use="required"/>
  </xsd:complexType>

  <xsd:complexType name="CT_TextBody">  <!-- text frame -->
    <xsd:sequence>
      <xsd:element name="bodyPr"   type="CT_TextBodyProperties"/>
      <xsd:element name="lstStyle" type="CT_TextListStyle"      minOccurs="0"/>
      <xsd:element name="p"        type="CT_TextParagraph"      maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:simpleType name="ST_Style">
    <xsd:restriction base="xsd:unsignedByte">
      <xsd:minInclusive value="1"/>
      <xsd:maxInclusive value="48"/>
    </xsd:restriction>
  </xsd:simpleType>
