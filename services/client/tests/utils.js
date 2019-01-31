export const clearLocalStorage = () => {
    localStorage.clear();
    localStorage.setItem.mockClear();
};