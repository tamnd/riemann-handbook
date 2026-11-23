---
id: li-stat
title: The local identity for the split of a Hermitian space
kind: theorem
decl: Formalism.HermitianLattices.Ext.L3.liStat
module: Formalism.GL3MeanSquares.GenusMeanAsymptotics.UnimodularClassRepresentatives.LiStatOf
covers: 467
status: drafted
drafted_by: writer@claude
---
This theorem proves `LIStat`, an identity at one prime $\mathfrak p$. It writes a weighted count of the orthogonal complements of a vector $x_0$ in a Hermitian lattice through the local density of $n = h(x_0, x_0)$. Its callers pass it to `massConst_all`, the induction on the dimension whose step is [the mass step](/entry/mass-const-succ/). In the spine it is below the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). The theorem only combines two lemmas; [`liRatio`](/entry/li-ratio/) has the main argument.

## Statement

Let $K$ be a totally complex field with an involution $a \mapsto \bar a$ that is complex conjugation at each embedding, such that for each prime $P$ of $\mathcal O_K$ some integer $\theta$ has $\theta - \bar\theta \notin P$ (`IsCMUnram`). Let $F$ be the fixed field (`IsFixF`). Let $(V, h)$ be a totally positive definite [[Hermitian form|8NJ7XY6F1S]] space over $K$ of dimension $m$. Let $V = K x_0 \oplus V'$ be an orthogonal split (the structure `VecSplit`), with $h' = h|_{V'}$ and $h(x_0, x_0) = n \in \mathcal O_F$, $n \neq 0$. Let $L$ be an integral $\mathcal O_K$-lattice in $V$ and $\mathfrak p$ a maximal ideal of $\mathcal O_F$ with norm $q$. Write $\eta(\mathfrak p) = -1$ if $\mathfrak p \mathcal O_K$ is prime and $1$ otherwise.

The local quantities are these.

- $L_{(\mathfrak p)}$: the localization of $L$ at $\mathcal O_F \setminus \mathfrak p$ (`locF`).
- $\alpha_{\mathfrak p}(L, n)$: the limit in $k$ of the number of classes $x \in L / \mathfrak p^k L$ with $h(x,x) \equiv n \bmod \mathfrak p^k$, divided by $q^{k(2m-1)}$ (`alphaN`).
- $\alpha_{\mathfrak p}(L, L)$: the limit of the number of endomorphisms of $L / \mathfrak p^k L$ that keep $h$ modulo $\mathfrak p^k$, divided by $q^{km^2}$ (`alphaL`).
- $d_{\mathfrak p}(L)$: the largest $e$ with $\operatorname{disc}(L) \subseteq (\mathfrak p \mathcal O_K)^e$ (`vd`).
- $\alpha_{\mathrm{std}}(r) = \prod_{j=1}^{r} (1 - \eta(\mathfrak p)^j q^{-j})$ and $\lambda_{\mathfrak p}(T) = \alpha_{\mathrm{std}}(r)\, q^{r\, d_{\mathfrak p}(T)} / \alpha_{\mathfrak p}(T, T)$ for a lattice $T$ of rank $r$ (`alphaStd`, `lamP`).
- $\psi_{\mathfrak p}(L) = \sum_T f(L, T)\, \lambda_{\mathfrak p}(T)$ (`psiP`). Here $T$ runs over representatives, up to isometry of $V'$, of the $\mathfrak p$-local integral lattices of $V'$ with $f(L,T) \neq 0$. The number $f(L, T)$ counts the lattices $\Lambda = g L_{(\mathfrak p)}$, with $g$ an isometry of $V$, such that $x_0 \in \Lambda$ and $\Lambda \cap V' = T_{(\mathfrak p)}$ (`fibLoc`).

**Theorem.**
$$\psi_{\mathfrak p}(L) = q^{(m-1)(v_{\mathfrak p}(n) + d_{\mathfrak p}(L))}\, \alpha_{\mathrm{std}}(m-1)\, \frac{\alpha_{\mathfrak p}(L, n)}{\alpha_{\mathfrak p}(L, L)}.$$

## Proof

Write $R(L) = q^{(m-1) d_{\mathfrak p}(L)}\, \alpha_{\mathfrak p}(L,n) / \alpha_{\mathfrak p}(L,L)$ (`repRatio`).

1. `liPin` gives one integral lattice $L_0$ with $R(L_0) \neq 0$ and $\psi_{\mathfrak p}(L_0) = q^{(m-1) v_{\mathfrak p}(n)}\, \alpha_{\mathrm{std}}(m-1)\, R(L_0)$.
2. [`liRatio`](/entry/li-ratio/) gives $\psi_{\mathfrak p}(L)\, R(L_0) = \psi_{\mathfrak p}(L_0)\, R(L)$.

Substitute 1 into 2 and cancel $R(L_0)$. Then $\psi_{\mathfrak p}(L) = q^{(m-1)v_{\mathfrak p}(n)} \alpha_{\mathrm{std}}(m-1) R(L)$, and the definition of $R(L)$ gives the theorem.

## In the Lean code

The theorem is in [LiStatOf.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/LiStatOf.lean#L24). It is `liStat_of liRatio liPin`, and `liStat_of` (line 11) is the algebra above. The statement `LIStat` is in [LocalDensityRatio.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/LocalDensityRatio.lean#L121). `LIRatio`, `LIPin` and `repRatio` are in [SigmaCount.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/SigmaCount.lean#L31). `liPin` is in [LiPin.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/LiPin.lean#L104); it rescales $h$ by $n^{-1}$ and calls `PinD.core`, which we have not unfolded.

If no set of representatives exists, `psiP` is $0$ by definition. The limits in `alphaN` and `alphaL` are `limUnder`. For `alphaN`, `alphaN_eq_of_le` shows that the quotient equals the limit once $k \geq 2 d_{\mathfrak p}(L) + 2 v_{\mathfrak p}(n) + 2$.
