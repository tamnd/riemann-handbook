---
title: First order Selmer bounds at Taylor-Wiles level
decls:
  - UpperTheory.V.Pa.W1_bound_arithmetic_rank_two
  - UpperTheory.V.Pa.b1abs
  - UpperTheory.V.Pa.b1Ar
status: drafted
drafted_by: writer@claude-opus-5-5
---
## First order Selmer bounds at Taylor-Wiles level

The rest of the chapter carries out a patching argument in the style of Taylor and Wiles for an ordinary, conjugate self-dual Galois representation and its generic first order thickening. This section sets up the frame and proves the first of two Selmer bounds that the argument needs. The bound says that a Selmer group of first order deformations, taken at Taylor-Wiles level $N$ and modulo $t^m$, has at most $\#K^{m D_0 + C}$ times as many elements as its coboundaries, with $D_0 = n[L^+ : \mathbb{Q}] + nq$ and $C$ independent of $m$ and $N$. The proof is an Euler characteristic count. For the background see [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology), [Selmer groups](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups) and [patching](/learn/deformations-patching/#taylor-wiles-kisin-patching).

### Local and global frames

Fix an odd prime $l$. *Local data* consist of a finite set $V$ and, for each $v \in V$, a compact totally disconnected group $G_v$ with a subgroup $I_v$, together with a finite set $U$ and, for each $u \in U$, a group $G_u$ of the same kind with a subgroup $J_u$. Think of $G_v$ as a decomposition group above $l$ and of $J_u$ as an inertia group at a place outside $l$.

A *global datum* over these local data is a compact totally disconnected group $\Gamma$ with a continuous character $\eta \colon \Gamma \to \{\pm 1\}$, an element $c$ with $c^2 = 1$ and $\eta(c) = -1$, a continuous character $\varepsilon \colon \Gamma \to \mathbb{Z}_l^\times$, and continuous homomorphisms $\varphi_v \colon G_v \to \Gamma_0$ and $\varphi_u \colon G_u \to \Gamma_0$, where $\Gamma_0 = \ker \eta$. The model is the Galois group of a totally real field $L^+$ acting through a CM extension $L$, with $\eta$ the sign of $L/L^+$, $c$ a complex conjugation and $\varepsilon$ the cyclotomic character. A morphism of global data is a continuous surjection that respects $\eta$, $c$, $\varepsilon$ and the maps from the local groups.

For a subgroup $H$ of $\Gamma$ let $\mathrm{PL}(H)$ be the intersection of the open normal subgroups $W$ of $\Gamma$ such that each element of $H$ has $l$-power order in $\Gamma/W$. Say that $\Gamma$ satisfies the *$\Phi$ condition* if each open subgroup has only finitely many continuous homomorphisms to $\mathbb{Z}/l$.

### Points and their first order thickening

A *point of rank $n$* is a finite field $K$, the ring $A = K[[t]]$ and a continuous representation $\rho \colon \Gamma_0 \to \mathrm{GL}_n(A)$, polarized by a form compatible with $c$ and trivial on the groups $\varphi_u(J_u)$. It comes with an integer $a$ with $1 \le a \le n$: every $\rho(g)$ is block diagonal for the decomposition $n = a + (n - a)$, and each block diagonal matrix, multiplied by a suitable power of $t$, is an $A$-linear combination of the matrices $\rho(g)$ with $g$ in a fixed subgroup $G'$ of $\Gamma_0$. At each $v \in V$ there are a matrix $w_v$ and characters $\psi_{v,1}, \dots, \psi_{v,n}$ such that $w_v^{-1} \rho(\varphi_v(g)) w_v$ is upper triangular with diagonal $(\psi_{v,i}(g))_i$. The characters are pairwise distinct, and $\psi_{v,i} \ne \psi_{v,j}\,\varepsilon$ for $i < j$. So $\rho$ is ordinary at every $v$. For a subgroup $D$ of $\Gamma_0$, condition $\mathrm{N}_4(D)$ says that the only matrix $Z$ with $\varepsilon(g)\rho(g) Z = Z \rho(g)$ for all $g \in D$ is $Z = 0$.

Call a matrix *even* if it is block diagonal and *odd* if it lives in the two off-diagonal blocks. The Selmer group of odd cocycles consists of the continuous cocycles $z \colon \Gamma_0 \to M_n(A)$ for the adjoint action, with odd values, with $z(c g c) = -z(g)^{T}$, vanishing on the $J_u$, and ordinary at each $v$: after conjugation by $w_v$ and subtraction of a coboundary, $z$ is upper triangular, with diagonal vanishing on a fixed subgroup $\mu_v$. A *basis of odd classes* is a family $\kappa_1, \dots, \kappa_g$ of such cocycles, linearly independent modulo coboundaries of odd antisymmetric matrices, such that each Selmer cocycle is, after multiplication by a power of $t$, a combination of the $\kappa_j$ modulo coboundaries.

For a ring $X$ over $A$ let $\mathrm{DD}_g(X) = X \oplus X^g \oplus X^g \oplus X$, with elements written $(a, e, e', h)$ and product

$$(a, e, e', h)(b, f, f', k) = \Bigl(ab,\ af + eb,\ af' + e'b,\ ak + hb + \sum_j (e_j f'_j + e'_j f_j)\Bigr).$$

So $\mathrm{DD}_g$ is the ring of first order thickenings in $2g$ variables $\epsilon_j, \epsilon'_j$ with $\epsilon_j \epsilon'_j$ equal to a common element $h$. The *first order thickening* of $\rho$ along the basis is

$$\rho_1(g) = \Bigl(1 + \sum_j \epsilon_j \kappa_j(g)\Bigr) \rho(g) \in \mathrm{GL}_n(\mathrm{DD}_g(X)).$$

Let $W_1$ be the matrices whose even entries lie in $X$ and whose odd entries lie in the $\epsilon$ part. For a morphism $h_N \colon \Gamma_N \to \Gamma$ let $\mathrm{Sel}_1$ be the Selmer group of $\rho_1 \circ h_N$ with values in $W_1$, with the ordinary conditions given by the thickened matrices $(1 - \sum_j \epsilon_j Y_{j,v}) w_v$, and let $\mathrm{Bd}_1$ be its coboundaries $g \mapsto \rho_1(g) Y \rho_1(g)^{-1} - Y$ with $Y \in W_1$ antisymmetric.

### Taylor-Wiles data

A *Taylor-Wiles datum* over a global datum $\Gamma$ consists of the following. There is an integer $q$ and an open normal subgroup $H \subseteq \Gamma_0$ on which $\varepsilon \equiv 1 \bmod l$. For each $N$ there are a global datum $\Gamma_N$ with a morphism $h_N \colon \Gamma_N \to \Gamma$, elements $\sigma_1, \dots, \sigma_q$ of $G'$, integers $N_{N,j} \equiv 1 \bmod l^N$ and elements $\phi_{N,j}, \tau_{N,j}$ of $\Gamma_{N,0}$ with:

1. $h_N(\tau_{N,j}) = 1$, $h_N(\phi_{N,j})\sigma_j^{-1} \in H$, and $h_N(\phi_{N,j}) \to \sigma_j$ modulo every open normal subgroup that contains $\mathrm{PL}(H)$;
2. the tame relation $\tau^{-N_{N,j}} \phi^{-1} \tau \phi \in \mathrm{PL}(h_N^{-1} H)$;
3. $\ker h_N$ lies in the closure of the normal subgroup generated by the $\tau_{N,j}$ and $\mathrm{PL}(h_N^{-1} H)$;
4. the number of continuous homomorphisms $h_N^{-1} H \to \mathbb{Z}/l$ is bounded independently of $N$, and the local groups satisfy the $\Phi$ condition.

These are the auxiliary places of Taylor and Wiles: $\phi_{N,j}$ is a Frobenius at a prime $\equiv 1 \bmod l^N$ and $\tau_{N,j}$ generates its tame inertia. The datum satisfies condition $\mathrm{Eig}(\alpha)$ for $\alpha \colon \{1, \dots, q\} \times \{1, \dots, n\} \to A$ if each $\rho(\sigma_j)$ has characteristic polynomial $\prod_i (X - \alpha_{j,i})$ with distinct roots.

Put $A_m = A/t^m$. The *first order bound* $\mathrm{B}_1(D_0)$ for a basis $\kappa$ says: there is $C$ such that for each $m$ and all large $N$, the group $\mathrm{Sel}_1$ with coefficients in $\mathrm{DD}_g(A_m)$ is finite and

$$\# \mathrm{Sel}_1 \le \# \mathrm{Bd}_1 \cdot \# K^{m D_0 + C}.$$

### Detection and local abelianization

The dual of $W_1$ is the module of matrices with even entries in the $h$ part and odd entries in the $\epsilon'$ part. Twisted cocycles with values there, for the action $Z \mapsto \varepsilon(g) \rho_1(g) Z \rho_1(g)^{-1}$ and with $z(cgc) = -\varepsilon(c) z(g)^{T}$, form a group $\mathrm{TwZ}$. For $\sigma \in \Gamma_0$ let $\ell_\sigma(z)$ be the $h$ component of $\operatorname{tr}(z(\sigma)\rho_1(\sigma))$. A set $S$ *detects* the basis if each $z \in \mathrm{TwZ}$ with $\ell_\sigma(z) = 0$ for all $\sigma \in S$ becomes a twisted coboundary after multiplication by a power of $t$.

A *local abelianization of rank $d$* for $(G_v, I_v)$ is a continuous surjection $G_v \to \mathbb{Z}_l^d \times \mathbb{Z}_l$ under which $I_v$ maps exactly onto $\mathbb{Z}_l^d \times 0$, and through which every continuous map to a finite abelian $l$-group that kills the roots of unity part factors. For the decomposition group of a place above $l$ of degree $d$ over $\mathbb{Q}_l$ this is [local class field theory](/learn/galois-cohomology/#local-fields).

An *arithmetic system* of degree $d$ and auxiliary group $D_0 \subseteq \Gamma_0$ records, for each $N$, an Euler characteristic count for $\Gamma_N$ with local degrees $d_v$ summing to $d$ and constant in $N$, an auxiliary local group whose image in $\Gamma_0$ is $D_0$, and local groups at the auxiliary places that contain $\phi_{N,j}$ and $\tau_{N,j}$.

**Theorem 7.8.1 (First order bound at Taylor-Wiles level).** Let $l \ne 2$. Let $\Gamma$ be a global datum with a Taylor-Wiles datum, $x$ a point of rank $n$ with a basis of odd classes $\kappa_1, \dots, \kappa_g$, $\alpha$ a family of eigenvalues, and suppose given an arithmetic system of degree $d$ with auxiliary group $D_0$. Let $d' \colon V \to \mathbb{N}$ with $\sum_v d'_v = d$, and suppose each $(G_v, I_v)$ has a local abelianization of rank $d'_v$. Assume that $\Gamma$ satisfies the $\Phi$ condition, that $\rho$ is trivial on $\Gamma_0 \cap \mathrm{PL}(H)$, that $\mathrm{N}_4(D_0)$ and $\mathrm{Eig}(\alpha)$ hold, and that $\{\sigma_1, \dots, \sigma_q\}$ detects the basis. Then $\mathrm{B}_1(nd + nq)$ holds.

Lean: `UpperTheory.V.Pa.W1_bound_arithmetic_rank_two` (also `UpperTheory.V.Pa.b1abs`).

*Proof.* Put $\nu = \binom{a}{2} + \binom{n-a}{2} + g a(n-a)$. Each term of the count below is bounded by a power of $\#K$ whose exponent is linear in $m$ with a constant independent of $m$ and $N$.

1. The invariants of $\Gamma_0$ on antisymmetric matrices in $W_1$ have at most $\#K^{c_1}$ elements.
2. Detection by $\{\sigma_j\}$ bounds the dual Selmer group: for all large $N$, a dual cocycle that is a coboundary at each auxiliary place lies in the coboundaries up to a factor $\#K^{c_2}$.
3. Condition $\mathrm{N}_4(D_0)$ bounds the $\varepsilon$-twisted invariants of $D_0$ on the dual by $\#K^{c_0}$.
4. At the auxiliary place $j$, the twisted invariants of $\rho_1(\sigma_j)$ on the dual have at most $\#K^{mn + C_j}$ elements. Here the distinct eigenvalues of $\rho(\sigma_j)$ enter: the centralizer of a regular semisimple matrix has rank $n$. For large $N$ the element $\phi_{N,j}$ acts on the coefficients modulo $t^m$ exactly as $\sigma_j$, with trivial twist by $\varepsilon$. This uses that $\rho$ is trivial on $\Gamma_0 \cap \mathrm{PL}(H)$ and that $h_N(\phi_{N,j}) \to \sigma_j$.
5. At $v \in V$, the local abelianization of rank $d'_v$ gives at most $\#K^{m(n(d'_v + 1) + \nu(1 + d_v)) + C_v}$ local classes.

Feed these bounds into the Euler characteristic count of the arithmetic system at level $N$, which compares $\# \mathrm{Sel}_1 \cdot \#\mathrm{H}^0$ with the product of the local terms and the dual Selmer group. Summing the exponents, with $\sum_v d'_v = \sum_v d_v = d$, gives

$$\# \mathrm{Sel}_1 \cdot \# K^{u} \le \# \mathrm{Bd}_1 \cdot \# K^{m(nd + nq) + C + u}, \qquad u = m(n + \nu)\#V + m\nu d,$$

with $C = c_1 + c_2 + c_0 + \sum_v C_v + \sum_j C_j$. Cancel $\# K^u$. $\square$

The constant $C$ depends on the point and on the basis but not on $m$ or $N$. That uniformity is what the patching argument needs.

### The arithmetic instance

Now let $L$ be a CM field with maximal totally real subfield $L^+$ and fix an ordinary Hida setting for $L$ at $l$, with a level $V_0$, a coefficient ring $\mathcal{O}$ and a residual datum $r$. These determine a global datum, and a family of Taylor-Wiles places determines a Taylor-Wiles datum. The published inputs of Galois cohomology are collected in one hypothesis: local finiteness, local Tate duality, the local and global Euler characteristic formulas, global finiteness, the formula of Greenberg and Wiles, normalized Poitou-Tate duality and the tame local computations. The hypothesis of local class field theory says that there are $d_v$ with $\sum_v d_v = [L^+ : \mathbb{Q}]$ such that each decomposition group above $l$ has a local abelianization of rank $d_v$.

**Theorem 7.8.2 (Arithmetic first order bound).** Assume the published inputs. Let $L$ be a CM field, fix a Hida setting with a level $V_0$ whose set of places is that of the setting, a coefficient ring $\mathcal{O}$ and a residual datum $r$ of rank $n$, and a Taylor-Wiles datum with Taylor-Wiles places. Assume local class field theory and that $\varepsilon \not\equiv 1 \bmod l$ on $\Gamma_0$. Let $x$ be a point with a basis of odd classes, trivial on $\Gamma_0 \cap \mathrm{PL}(H)$, with $\mathrm{N}_4$ for the auxiliary group of $V_0$, with $\mathrm{Eig}(\alpha)$, and such that $\{\sigma_j\}$ detects the basis. Then $\mathrm{B}_1(n[L^+ : \mathbb{Q}] + nq)$ holds.

Lean: `UpperTheory.V.Pa.b1Ar`.

*Proof.* Local class field theory gives $d'$ with $\sum_v d'_v = [L^+ : \mathbb{Q}]$ and the local abelianizations. The published inputs and the Taylor-Wiles places give an arithmetic system of degree $[L^+ : \mathbb{Q}]$, and they give the $\Phi$ condition for $\Gamma$. Apply the first order bound. The only remaining step converts the finite sum over places in the hypothesis to a sum over the finite set $V$. $\square$

This bound and the obstruction bound of the next section are the two Selmer inputs of every point that enters the patching argument.

**Remark 7.8.3 (Formalization).** The name `W1_bound_arithmetic_rank_two` is misleading: the statement in [W1BoundArithmeticRankTwo.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/EpsilonEtaMatrices/W1BoundArithmeticRankTwo.lean#L40) is for any rank $n$ and makes no use of rank two. `b1abs` in [B1abs.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/EpsilonEtaMatrices/B1abs.lean#L12) is a second name for the same statement, proved by quoting it. The Euler characteristic count is the lemma `oneLevel`, and the final cancellation is the private lemma `cancel_pow`. In `b1Ar` ([BoundW1Arithmetic.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/AutomorphicDetection/BoundW1Arithmetic.lean#L8)) the hypothesis that $\varepsilon \not\equiv 1 \bmod l$ is bound to `_` and never used. The conversion of `finsum` to a `Finset` sum at line 14 is written as a `first | exact … | convert …` fallback rather than a single proof. The objects `NP`, `Kap`, `DD`, `Sel1`, `Bd1`, `TWGrp` and `Detects` are defined in [PairedDualFirstOrderDualMatrixSpace.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/PairedDualFirstOrderDualMatrixSpace.lean#L251) and [ThetaCoefficientMapEq.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ThetaCoefficientMapEq.lean#L15).
