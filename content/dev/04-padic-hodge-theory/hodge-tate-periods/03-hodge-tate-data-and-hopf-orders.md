---
title: Hodge-Tate data and Hopf orders
decls:
  - GlobalTheory.EvClose.htdOfDat
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hodge-Tate data and Hopf orders

A period datum of [the first section](/entry/period-datum-main/) records the $p$-torsion of $G$ in two ways: as points $\tau_i(0)$ with their Weil pairings and periods, and through the coordinate ring of the finite flat group scheme $G[p]$. This section puts the second way in terms of the first. We evaluate the functions of $G[p]$ at the points $\sum_j t_j \tau_j(0)$, for $t \in (\mathbb{Z}/p)^{2g}$, and obtain an $\mathcal{O}$-lattice of $C$-valued functions on $(\mathbb{Z}/p)^{2g}$. It is a Hopf order. It is stable under the action of $O_e$, it contains the Hodge-Tate and lift periods modulo $p$, and its cotangent space is $\mathcal{O}^g/p$. These facts make a *Hodge-Tate datum*. The step [every character of the literature](/step/every-character-of-literature/) uses the Hodge-Tate datum of a period datum directly, and the next sections derive length bounds from it.

We keep the notation of the first section. Write $\mathrm{Ix}$ for the index set of size $2g$, $T = \mathbb{Z}_p^{\mathrm{Ix}}$ and $N = (\mathbb{Z}/p)^{\mathrm{Ix}}$, with reduction $t \mapsto \bar t$ from $T$ to $N$. For a matrix $E \in M_{\mathrm{Ix}}(\mathbb{Z}_p)$ put $\langle s, t \rangle_E = s^{\mathsf T} E t$. Let $R$ be a ring with a map $R \to C$, and write $\mathrm{Fun}(N, C)$ for the $C$-valued functions on $N$.

### Hopf orders in the functions on a finite group

The functions on the finite abelian group $N$ form the Hopf algebra of the constant group scheme $N$ over $C$. A finite flat model of this group over $R$ corresponds to an $R$-form of this Hopf algebra. The next definition says this with functions.

**Definition 4.3.1 (Hopf order).** An $R$-submodule $\Omega \subseteq \mathrm{Fun}(N, C)$ is a *Hopf order* if:

1. $\Omega$ is a lattice: it is the $R$-span of the columns of a matrix $M \in M_N(C)$ with $\det M \neq 0$;
2. each $f \in \Omega$ takes values in the image of $R$;
3. $1 \in \Omega$, and $\Omega$ is closed under products;
4. for $f \in \Omega$, the function $(x, y) \mapsto f(x + y)$ on $N \times N$ is in the $R$-span of the functions $(x, y) \mapsto f_1(x) f_2(y)$ with $f_1, f_2 \in \Omega$;
5. for $f \in \Omega$, the function $x \mapsto f(-x)$ is in $\Omega$.

The *augmentation ideal* $I_\Omega$ is the set of $f \in \Omega$ with $f(0) = 0$, and $I_\Omega^2$ is the $R$-span of the products $f f'$ with $f, f' \in I_\Omega$. The quotient $I_\Omega/I_\Omega^2$ is the *cotangent module* of $\Omega$.

**Example 4.3.2.** The functions $N \to C$ with values in the image of $R$ form a Hopf order, the functions of the constant group $N$ over $R$. Its augmentation ideal is spanned by the idempotents $\delta_x$ with $x \neq 0$, so $I_\Omega = I_\Omega^2$ and its cotangent module is $0$. This is the étale case. The Hopf order of $G[p]$ below is of the opposite kind: its cotangent module is $(\mathcal{O}/p)^g$, the cotangent space of $G$ modulo $p$.

**Definition 4.3.3 (Hodge-Tate datum).** Let $R$ be a $\mathbb{Z}_p$-algebra with a map $R \to C$, let $O_e$ be a commutative $\mathbb{Z}_p$-algebra with an involution $\sigma$, and let $c_p \in R$. A *Hodge-Tate datum* for $(O_e, \sigma, c_p)$ consists of Hodge-Tate data $(\rho, \rho_L, P, P_L, E, H, B)$ over $R$ as in [the first section](/entry/period-datum-main/), a Hopf order $\Omega \subseteq \mathrm{Fun}(N, C)$ over $R$, and an $R$-linear map $\varphi : I_\Omega \to (R/p)^g$, such that:

1. for $a \in O_e$ and $f \in \Omega$ there is $f' \in \Omega$ with $f'(\bar t) = f(\overline{\rho(a) t})$ for all $t \in T$;
2. for each $k$ there are $f, f' \in \Omega$ with $(Ht)_k \equiv f(\bar t)$ and $(Bt)_k \equiv f'(\bar t)$ modulo $pR$ for all $t \in T$;
3. if $p = 2$, then for each $s \in T$ the function $\bar t \mapsto (-1)^{\langle s, t \rangle_E}$ is in $\Omega$;
4. $\varphi$ is surjective with kernel $I_\Omega^2$;
5. if $f, f' \in I_\Omega$ with $f'(\bar t) = f(\overline{\rho(a)t})$ for all $t$, and $\varphi(f) = l \bmod p$, then $\varphi(f') = \rho_L(a)^{\mathsf T} l \bmod p$.

So a Hodge-Tate datum is a Hopf order with an action, whose cotangent module is $(R/p)^g$ with the action $\rho_L^{\mathsf T}$, and whose functions see the period matrices modulo $p$. A *Hodge-Tate setting* for $(R, O_e, \sigma, c_p)$ is the following list of conditions: $R$ is the ring of integers of $v$, $0 < v(p) < 1$, $v(c_p)^{p-1} = v(p)$, and $\sigma$ is an involution. For $c_p = \zeta_p - 1$ the condition on $v(c_p)$ is the classical identity $v(\zeta_p - 1)^{p-1} = v(p)$.

### The evaluation image

Let $D$ be a period datum of a framed group $\mathcal{B}$ over a thickening tower with ring $\mathcal{O}$, and let $\mathcal{O} \to C$ be a ring map. The datum gives finite free $\mathcal{O}$-algebras $A_i$ and points $y_i \in G(A_i)[p]$ that represent the $p$-torsion. For $t \in N$ the point $x_t = \sum_j t_j \tau_j(0)$ of $G(\mathcal{O})[p]$ is the image of $y_{i(t)}$ under a unique index $i(t)$ and a unique $\mathcal{O}$-algebra map $\varphi_t : A_{i(t)} \to \mathcal{O}$.

**Definition 4.3.4 (Evaluation image).** For $F = (F_i) \in \prod_i A_i$ let $\mathrm{ev}(F) \in \mathrm{Fun}(N, C)$ be $t \mapsto \varphi_t(F_{i(t)})$. The *evaluation image* $\Omega_D$ is the $\mathcal{O}$-span of the functions $\mathrm{ev}(F)$.

So $\Omega_D$ is the coordinate ring of $G[p]$ over $\mathcal{O}$, read through its values at the $p^{2g}$ points $x_t$.

**Lemma 4.3.5 (The evaluation image).** Let $D$ be a period datum, and let $\mathcal{O} \to C$ be injective with $\mathcal{O}$ a domain. Then:

1. $\Omega_D$ is a lattice in $\mathrm{Fun}(N, C)$ with values in $\mathcal{O}$, it contains $1$, and it is closed under products;
2. $\Omega_D$ satisfies conditions 4 and 5 of a Hopf order;
3. $\Omega_D$ is stable under $\rho$ in the sense of condition 1 of a Hodge-Tate datum;
4. the rows of $H$ and of $B$ agree modulo $p$ with functions in $\Omega_D$, as in condition 2;
5. if $p = 2$, the functions $\bar t \mapsto (-1)^{\langle s, t\rangle_E}$ are in $\Omega_D$;
6. there is a map $\varphi : I_{\Omega_D} \to (\mathcal{O}/p)^g$ with the properties 4 and 5 of a Hodge-Tate datum.

Lean: `GlobalTheory.EvClose.evLat`, `GlobalTheory.EvClose.evHopf`, `GlobalTheory.EvClose.evAct`, `GlobalTheory.EvClose.evHt`, `GlobalTheory.EvClose.evBt`, `GlobalTheory.EvClose.periodDatum_signCharacters_mem_evalImage`, `GlobalTheory.EvClose.evCot`.

*Proof.* Each part is a result of its own, and we say what each uses. Part 1: the evaluation map $\prod_i A_i \to \mathrm{Fun}(N, C)$ is a ring map. It is injective because the functions of each $A_i$ are separated by its $\mathcal{O}$-points, and the total rank $\sum_i \operatorname{rank} A_i$ is $\#G(\mathcal{O})[p] = \#N$. So the image is a lattice of full rank, and its values lie in $\mathcal{O}$. Part 2 comes from the group law of $G[p]$: the sum of two $p$-torsion points is represented over the tensor products $A_i \otimes_{\mathcal{O}} A_j$, which are local because they are finite and have points. Part 3 comes from the naturality of the action of $O_e$ on the $p$-torsion, together with $a \cdot \tau_j(0) = \sum_k \rho(a)_{kj} \tau_k(0)$. Parts 4 and 6 use the formal chart. Modulo $p$, the local factors $A_i/p$ map onto $K$ with nilpotent kernel, so the chart gives coordinates of the points $y_i$. For part 4 the Hodge-Tate period of $x_t$ is a linear function of these coordinates. For the lift periods the proof also uses the $p$-series of $F$ and the Frobenius of the Witt thickening $W$. Part 6 uses the universal derivation of the Hopf order: the cotangent module of the coordinate ring of $G[p]$ is $\omega_G/p$, and the points of the chart identify it with $(\mathcal{O}/p)^g$. Part 5 uses the Weil pairing at level $p$: for $p = 2$ we have $\zeta_0 = -1$, so bilinearity and the matrix $E$ give $e_2(x_s, x_t) = (-1)^{\langle s, t\rangle_E}$, and the proof shows that this function of $t$ comes from the coordinate ring of $G[2]$. $\square$

**Proposition 4.3.6 (The Hodge-Tate datum of a period datum).** Let $D$ be a period datum of a framed group for $(O_e, \sigma, c_p)$, let $\mathcal{O} \to C$ be injective with $\mathcal{O}$ a domain, and let $v$ be a valuation of $C$. Then the Hodge-Tate data of $D$, the Hopf order $\Omega_D$ and the map $\varphi$ of the lemma form a Hodge-Tate datum over $\mathcal{O}$ for $(O_e, \sigma, c_p)$.

Lean: `GlobalTheory.EvClose.htdOfDat`.

*Proof.* This is the lemma above applied to $D$: parts 1 and 2 make $\Omega_D$ a Hopf order, and parts 3 to 6 are the conditions 1 to 5 of a Hodge-Tate datum. The matrices $\rho, \rho_L, P, P_L, E, H, B$ and their relations are those of $D$. $\square$

For the $A_{\mathrm{inf}}$ tower, $\mathcal{O}$ is the ring of integers of $v$, so the map $\mathcal{O} \to C$ is injective and $\mathcal{O}$ is a domain. So each period datum of [the theorem on abelian schemes](/entry/abelian-period-datum-main/) gives a Hodge-Tate datum, with $c_p = \zeta_p - 1$, and the conditions of a Hodge-Tate setting hold.

**Remark 4.3.7 (Formalization).** The proposition is a definition in Lean, which builds the Hodge-Tate datum from seven results, one for each part of the lemma. The valuation $v$ is a parameter of a Hodge-Tate datum, but no condition of the datum mentions it; it enters only through a Hodge-Tate setting. So the proposition holds for any $v$. The datum stores the cotangent map as a choice from part 6. We have opened the statements of the seven results, not their proofs; the description of their proofs above follows the results that they cite.
