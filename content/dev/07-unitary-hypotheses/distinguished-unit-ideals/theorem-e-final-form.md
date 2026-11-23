---
id: theorem-e-final-form
title: Theorem E for lattices over power series, in final form
kind: theorem
decl: Formalism.ExponentWindows.E.theorem_E_final_form
module: Formalism.DistinguishedUnitIdeals.DistinguishedOrderProofs.ThmEFinal
covers: 714
status: drafted
drafted_by: writer@claude
---
This theorem is the abstract lifting statement behind [the lifting theorem for crystalline lattices](/entry/crystalline-lifting-second-form/). It says that $\ell^E$ times each cocycle of the target lifts to the source up to a coboundary. The proof reduces it to [theorem E in primitive form](/entry/theorem-e-primitive-form/).

## Statement

Let $\mathcal{O}$ be a discrete valuation ring with an irreducible element $\varpi$. A *base* is a natural number $\ell$ and two commuting $\mathcal{O}$-algebra endomorphisms $\varphi, \gamma$ of $\mathcal{O}[[X]]$. Put $p_s = \varphi^s(X + \ell)$.

A *lattice* is an $\mathcal{O}[[X]]$-module $V$ with additive maps $\varphi_i, \gamma_i$ and submodules $N_i$, for $i \in \mathbb{Z}/n$. The maps are semilinear over $\varphi$ and $\gamma$, and $\varphi_i \gamma_{i-1} = \gamma_i \varphi_i$. A pair $(y, z)$ of maps $\mathbb{Z}/n \to V$ is a *coboundary* if there is $m$ with $y_i = \varphi_i(m_{i-1}) - m_i$ and $z_i = \gamma_i(m_i) - m_i$. A map of lattices is linear, commutes with $\varphi_i$ and $\gamma_i$, and maps $N_i$ into $N_i$.

*Cuts* are a nonempty set of indices $c$ with lengths $1 \le \ell_c \le n$, such that $c - \ell_c$ is a cut and no cut lies strictly between.

**Theorem.** Let $h \colon L_1 \to L_2$ be a map of lattices, $L_0$ a lattice with $e_0 \in L_0$, and $Z_1, Z_2$ additive groups of pairs. Fix window data and integers $j, g, G_0, S, \eta, h_h, \sigma, r, \kappa, \ell_{\max}$. Assume:

1. (`FinalBase`) $\ell \ge 3$ is prime and associated to $\varpi^{e}$ with $e \ge 1$, $\mathcal{O}$ is $\ell$-adically complete, $\varphi$ and $\gamma$ satisfy `E3` and `E4`, a unit $u$ equals $1 + \ell x$, and the field `LL` is a fraction field of $\mathcal{O}$;
2. (`FinalNum`) inequalities such as $G_0, S, \eta \le g \le h_h$ and $1 \le j \le \ell_c \le \ell_{\max}$, the kind "thin" at the $j$ indices after each cut, a condition `SigOK` on $\sigma$, a condition `TextWord` on the order of kinds along each arc, and bounds of `kapExp` by $\kappa$;
3. (`FinalLat`) for $L_1$ and $L_2$: the conditions of `PrimLat` (among them `P9`, `P5M` and freeness), a Frobenius bound at each index, and multiplication by $X$ and by each $p_s$ is bijective;
4. (`PrimUnit`) $\varphi_i$ and $\gamma_i$ fix $e_0$, and $N_i(L_0) = \mathcal{O}[[X]]\, e_0$;
5. (`PrimBK`) $Z_1$ is stable under $\mathcal{O}$ and contains given cocycles, and each element of $Z_2$ is represented by an extension `Ext L₂ L₀` with the conditions `PrimExt`;
6. (`WPrimeCuts`) $\ell^r N_c(L_2) \subseteq h(N_c(L_1))$ at each cut $c$;
7. (`FinalArc`) the arc data at each cut, as in [`finalArc_holds`](/entry/final-arc-holds/).

Then for each $z \in Z_2$ there is $z' \in Z_1$ such that $\ell^E z - h(z')$ is a coboundary in $L_2$, where $E = 2r + 4\sigma + 2A + 2\kappa$ and $A = 2\sigma + r + 2g\,\ell_{\max}$.

We have not unfolded `E3`, `E4`, `P9`, `P5M` and `PrimExt`.

## Proof

The proof applies [theorem E in primitive form](/entry/theorem-e-primitive-form/) to the primitive parts of hypotheses 1 to 3 and to hypotheses 4 and 5. At each cut, `primArc` turns `FinalArc` into the primitive arc `PrimArc`. That step uses the rest of hypotheses 2 and 3, hypothesis 6, and lemmas on the level models, among them `partners_model_holds`, `constant_term_fourth_form` and `partner_fourth_fourth_form`.

## In the Lean code

The theorem is at [ThmEFinal.lean](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEFinal.lean#L513), and `primArc` at [line 417](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEFinal.lean#L417). The statement `ThmEFinal` is at [FinalArcProps.lean](lean:Formalism/DistinguishedUnitIdeals/FinalArcProps.lean#L226).

- $Z_1$ and $Z_2$ are free parameters. Only hypothesis 5 ties them to cocycles.
- The element $m$ of a coboundary may be any map $\mathbb{Z}/n \to V_2$; it need not lie in the $N_i$.
