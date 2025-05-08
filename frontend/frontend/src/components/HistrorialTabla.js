import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const HistorialTabla = ({ historialData }) => {
    return (
        <TableContainer component={Paper}>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Fecha</TableCell>
                        <TableCell>Acetona</TableCell>
                        <TableCell>Resultado</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {historialData.map((row, index) => (
                        <TableRow key={index}>
                            <TableCell>{row.fecha}</TableCell>
                            <TableCell>{row.acetona}</TableCell>
                            <TableCell>{row.resultado}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
};

export default HistorialTabla; 