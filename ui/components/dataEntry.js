import React from 'react';
import { Select, Space } from 'antd';


const NormalSelect = ({options, handleChange, value, defaultValue=""}) => (
  <Space wrap>
    <Select
        value={value}
        defaultValue={defaultValue}
        style={{ width: 'max-value' }}
        onChange={handleChange}
        options={options}
    />
  </Space>
);

export {NormalSelect};