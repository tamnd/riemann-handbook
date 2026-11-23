---
id: local-units-roots-main
title: Nonvanishing of the zeta class from the Coleman core and two inputs
kind: theorem
decl: UpperTheory.Kd.C7.LocalUnitsRoots.main
module: Development.AutomorphicArithmetic.Foundations.IwahoriReduction.LangPolynomials.NormFactorLeOne
covers: 483
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ZetaEulerSystemNonvanishing}(\mathrm{Pin7})$ from two hypotheses, which [`pLocu`](/entry/p-locu/) fills with two theorems. The main work is in [`pCore`](/entry/p-core/); this proof checks that the data of $\mathrm{Pin7}$ meet the hypotheses of `pCore` and closes by contradiction.

## Statement

Write $x \equiv_n x'$ for $|x - x'| \le |\ell^n|$ in $\overline{\mathbb{Q}}_\ell$. For a power series $L$ and $\varphi$ a character mod $\ell$, let $I_r(L)$ be the moment $\sum_{x<\ell^r,\ \ell\nmid x} \varphi(x)x^e\,\mathrm{mass}(L, r, \xi, x)$, with $\xi$ a primitive $\ell^r$-th root of unity.

The data are as in [`pLocu`](/entry/p-locu/) and [the unramified zeta theorem](/entry/zeta-ur/). $\mathrm{SpLink}$ says that $y(s)_2 \equiv_n \sum_x x^{-e}\chi_r(x) Z_r(s)(x)$ for $r$ large, for $s$ in inertia with $\bar\chi(s) = 1$. $\mathrm{Pin7}$ gives: a function $\nu$ equal to 1 on inertia, with $\nu(\sigma_0) = a$ at a Frobenius $\sigma_0$; units $a, a'$, $\kappa \neq 0$ and units $v'_m$ with $v'_{m+1} \equiv_m v'_m$; an embedding $j$, integral on $A$; a power series $L$ with integral coefficients; roots of unity $\zeta_m$ and, for $m \ge m_0$, a Kummer presentation of $Z_m$ by units $P_i(\zeta_m)$; congruences mod $\ell^{m-c_0}$ that link the log-derivative sums of the $P_i$ to the twisted sums $v'_m\kappa a'^m\sum_b \psi(b)\,\mathrm{tval}(L)(\zeta^b)$; $\chi_r = \varphi^{-1}$; and $I_r(L) \not\equiv_{n_0+r} 0$ for $r$ large.

The hypotheses:

- (H48) If two such twisted sums of $G$ and $L$ agree mod $\ell^{m-c_1}$ up to the factor $1 - c\,\psi^{-1}(c)$, with $\ell \nmid c$, and $I_r(L) \not\equiv_{n_0+r} 0$ for $r$ large, then $I_r(G) \not\equiv_{n_1+r} 0$ for some $n_1$ and $r$ large.
- (H50) Under $\mathrm{Nf}$ and $\mathrm{SrcUr}$, $W(s)_{22} = 1$ on inertia with $\bar\chi(s) = 1$.

**Theorem.** (H48) and (H50) imply $\mathrm{ZetaEulerSystemNonvanishing}(\mathrm{Pin7})$.

## Proof

Suppose $\mathrm{NzAt}$ fails.

1. By (H50), $y(s)_2 = 0$ for $s$ in inertia with $\bar\chi(s) = 1$. With $\mathrm{SpLink}$ and $\chi_r = \varphi^{-1}$, the twisted sums of $Z_r$ against $\varphi(x)^{-1}x^{-e}$ tend to 0: this is $\mathrm{SpZero}(\varphi, e, Z)$.
2. Since $\nu = 1$ on inertia, $\mathrm{IwSys2}$ gives the inertia cocycle conditions $\mathrm{IwI}$.
3. Frobenius law. `conj_law` gives $Z_m(\sigma s\sigma^{-1})(1) = \nu(\sigma)Z_m(s)(1)$ for $s$ in inertia with trivial cyclotomic character mod $\ell^m$. Two Frobenius elements differ by inertia (`pFrobEx`), so $\nu(\sigma) = a$.
4. `pCore` with $d_0 = 2$ gives a power series $G$, units $v_m$, and the two clauses of `pCore`.
5. Apply (H48) with $c = 2$. Its hypothesis is the chain: the $\mathrm{Pin7}$ congruence for $L$, the congruence for the log-derivative sums, and clause 1 of `pCore`. Each is multiplied by $1 - 2\psi^{-1}(2)$, of norm at most 1 (`norm_factor_le_one`). So $I_r(G) \not\equiv_{n_1+r} 0$ for $r$ large.
6. Clause 2 of `pCore` turns $\mathrm{SpZero}$ into $I_r(G) \equiv_{n_1+r} 0$ for $r$ large. This is a contradiction.

## In the Lean code

The theorem is `private`, at [NormFactorLeOne.lean, line 99](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/NormFactorLeOne.lean#L99). $\mathrm{Pin7}$ is in [HTPresNuOfPolys.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/HTPresNuOfPolys.lean#L24), and $\mathrm{SpLink}$ in [IsLocallyConstantCycMod.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/IsLocallyConstantCycMod.lean#L35). It calls:

- `pCore`, at [line 137](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/NormFactorLeOne.lean#L137);
- `pFrobEx`, in [FrobEx.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/FrobEx.lean#L23); only its clause on two Frobenius elements is used;
- the private helpers `conj_law`, `roots_pow`, `norm_factor_le_one` and the congruence rules `cg_symm`, `cg_trans`, `cg_mono`, `cg_mul`.

The letter $c_0$ has two uses. In $\mathrm{Pin7}$ it is a loss of precision; in (H48) it is the integer of the Euler factor, set to 2. The $c_0$ of $\mathrm{Pin7}$ enters (H48) as the precision $\max(c_0, c_1)$.
