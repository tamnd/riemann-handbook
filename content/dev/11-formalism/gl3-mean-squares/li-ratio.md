---
id: li-ratio
title: The local identity does not depend on the lattice
kind: theorem
decl: Formalism.HermitianLattices.Ext.L3.liRatio
module: Formalism.GL3MeanSquares.GenusMeanAsymptotics.UnimodularClassRepresentatives.RepRatioEqZero
covers: 339
status: drafted
drafted_by: writer@claude
---
This theorem proves `LIRatio`: for two integral lattices $L$ and $L_0$ in the same split Hermitian space, the two sides of the local identity have the same ratio. Its only caller is [the local identity](/entry/li-stat/), which computes the ratio for one chosen lattice $L_0$ and gets it for all $L$.

## Statement

Use the data and notation of [the local identity](/entry/li-stat/): $K$, $F$, $(V, h)$ of dimension $m$, the split $V = K x_0 \oplus V'$ with $h(x_0, x_0) = n \neq 0$, a maximal ideal $\mathfrak p$ of $\mathcal O_F$ of norm $q$, the sum $\psi_{\mathfrak p}$ and the local densities. Let
$$R(L) = q^{(m-1) d_{\mathfrak p}(L)}\, \frac{\alpha_{\mathfrak p}(L, n)}{\alpha_{\mathfrak p}(L, L)}.$$

**Theorem.** For integral lattices $L$ and $L_0$ of $V$,
$$\psi_{\mathfrak p}(L)\, R(L_0) = \psi_{\mathfrak p}(L_0)\, R(L).$$

## Proof

Put $\nu(T) = \alpha_{\mathfrak p}(T,T) / q^{r\, d_{\mathfrak p}(T)}$ for a lattice $T$ of rank $r$ (`nu`). Then $\lambda_{\mathfrak p}(T) = \alpha_{\mathrm{std}}(r) / \nu(T)$ (`eigenvalue_eq₂`). The proof has two cases.

**Case 1: some integral lattice $M_2$ has $x_0 \in M_{2,(\mathfrak p)}$.** Choose sets $s$ and $s_0$ of local representatives for $L$ and $L_0$ (`exists_locReps`). Then `psiP_eq_sum` gives
$$\psi_{\mathfrak p}(L) = \alpha_{\mathrm{std}}(m-1) \sum_{T \in s} \frac{f(L, T)}{\nu(T)},$$
and the same for $L_0$. The lemma `main_term` counts the solutions of $h(x,x) \equiv n \bmod \mathfrak p^k$ in $L / \mathfrak p^k L$ by the orbits of the lattices through $x_0$. For large $J$ and then large $k$ it gives
$$\#\{x\} = \kappa_{J,k} \cdot q^{d_{\mathfrak p}(L)} \nu(L) \cdot \sum_{T \in s} \frac{f(L, T)}{\nu(T)},$$
where $\kappa_{J,k}$ (`kap`) depends only on $M_{2,(\mathfrak p)}$, not on $L$. The lemma `repRatio_eq`, with `alphaN_eq_of_le`, turns this into $R(L) = \kappa_{J,k}\, q^{-k(2m-1)} \sum_{T \in s} f(L,T)/\nu(T)$. So $\psi_{\mathfrak p}(L)$ and $R(L)$ are two multiples of the same sum, with factors that do not depend on $L$. The cross products agree.

**Case 2: no such $M_2$.** Then `repRatio_eq_zero` gives $R(L) = R(L_0) = 0$, and both sides are $0$. In its proof, the set of orbit representatives from `exists_mReps` is empty, so the count is eventually $0$ by `nkCount_eq_sum`.

## In the Lean code

The theorem is in [RepRatioEqZero.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/RepRatioEqZero.lean#L68), with `eigenvalue_eq₂`, `repRatio_eq` and `repRatio_eq_zero` above it in the same file. It calls:

- `main_term` in [NuGmapLocF.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/NuGmapLocF.lean#L34), which uses `exists_mReps`, `nkCount_eq_sum` and `kap_eq`;
- `exists_locReps` and `psiP_eq_sum` in [ExistsGlobalOfFibLocNeZero.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/ExistsGlobalOfFibLocNeZero.lean#L19);
- `alphaN_eq_of_le` in [TendstoMeanAlphaN.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/TendstoMeanAlphaN.lean#L110).

We have not unfolded `kap_eq` or the count `cnt` inside `kap`.

Case 2 looks empty. Take $M_2 = \mathcal O_K x_0 + T$ with $T$ an integral lattice of $V'$. It is integral, because $h(x_0,x_0) = n$ is integral and $x_0 \perp V'$. The Lean proof does not use this; it treats the case directly.
