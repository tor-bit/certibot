import React from 'react';
import { Select, Space } from 'antd';

// TO NOTE: ADD THE SEARCH FUNCTIONALITY
const NormalSelect = ({options, handleChange, value, defaultValue="", labelInValue=false}) => (
  <Space wrap>
    <Select
        value={value}
        defaultValue={defaultValue}
        style={{ width: 'max-value' }}
        onChange={handleChange}
        options={options}
        labelInValue={labelInValue}
    />
  </Space>
);

const MultipleSelect = () => (
  <Space wrap>
    <Select
        value={value}
        defaultValue={defaultValue}
        style={{ width: 'max-value' }}
        onChange={handleChange}
        options={options}
        labelInValue={labelInValue}
    />
    <Select
      mode="multiple"
      allowClear
      style={{ width: '100%' }}
      placeholder="Please select"
      defaultValue={['a10', 'c12']}
      onChange={handleChange}
      options={options}
    />
  </Space>
);

export {NormalSelect, MultipleSelect};