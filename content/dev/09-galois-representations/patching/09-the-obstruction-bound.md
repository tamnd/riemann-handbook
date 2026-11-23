---
title: The obstruction bound
decls:
  - UpperTheory.V.Pa.B2.obstructionBound_of_duality
  - UpperTheory.V.Pa.b2Ar
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The obstruction bound

The first order bound of the previous section controls the tangent space of the patched deformation ring. The patching argument also needs control of the obstructions. This section proves that, at Taylor-Wiles level and modulo $t^m$, among any $g + 1$ families of even Selmer classes some combination with a unit coefficient lifts, after multiplication by a fixed power of $t$, to the second order thickening. The proof reduces the lifting problem to a second cohomology group with local conditions, bounds the size of that group by duality and Euler characteristics, and then applies a counting lemma for modules over a discrete valuation ring. See [Selmer groups](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups), [global fields](/learn/galois-cohomology/#global-fields) and [discrete valuation rings](/learn/commutative-algebra/#regular-local-rings-and-discrete-valuation-rings).

### Cohomological axioms

Let $\Gamma$ be a global datum over local data with places $V$ and $U$. Below, a *coefficient module* is a finite discrete module $M$ over a ring, with a continuous action, killed by $l$. Fix $d \in \mathbb{N}$ and $d_v \in \mathbb{N}$ for $v \in V$. The *cohomological axioms* for $(\Gamma, d, (d_v))$ are:

1. $\sum_v d_v = d$;
2. for every coefficient module, $\mathrm{H}^1$ and $\mathrm{H}^2$ of $\Gamma$, of each $G_v$ and of each $G_u$ are finite;
3. $\mathrm{H}^2(\Gamma, -)$ is right exact on coefficient modules: a surjection $M \to M'$ induces a surjection on $\mathrm{H}^2$;
4. there are $c_1, \dots, c_d \in \Gamma$ with $\eta(c_i) = -1$ and $c_i^2 = 1$ such that, for every coefficient module,
$$\#\mathrm{H}^0(\Gamma, M) \cdot \#\mathrm{H}^2(\Gamma, M) \cdot \#M^{d} = \#\mathrm{H}^1(\Gamma, M) \cdot \prod_{i=1}^{d} \#M^{c_i = 1};$$
5. for every coefficient module, $\#\mathrm{H}^1(G_v, M) = \#\mathrm{H}^0 \cdot \#\mathrm{H}^2 \cdot \#M^{d_v}$, and the same formula with exponent $0$ holds for $G_u$;
6. for $M$ trivial on $J_u$, the unramified classes have at least $\#\mathrm{H}^0(G_u, M)$ elements, and unramified cocycles lift along surjections;
7. for each finite coefficient datum, the cokernel of the global to local map in degree $2$ has at most as many elements as the group of additive maps $f \colon M \to \mathbb{Z}/l$ with $f(gm) = \varepsilon(g) f(m)$.

Axiom 4 is the global Euler characteristic formula of Tate for a totally real field of degree $d$, with $c_i$ the complex conjugations. Axiom 5 is the local formula for a place above $l$ of degree $d_v$ and for a place outside $l$. Axiom 7 is a consequence of Poitou-Tate duality.

### The second order condition

Keep the notation of the previous section: a point $x$ of rank $n$ with ring $A = K[[t]]$, a basis $\kappa_1, \dots, \kappa_g$ of odd classes, the ring $\mathrm{DD}_g$ and the first order thickening $\rho_1$. Let $W_2$ be the matrices whose even entries lie in the $\epsilon'$ part of $\mathrm{DD}_g$ and whose odd entries lie in the $h$ part. Let $\mathrm{Sel}_2$ be the Selmer group of $\rho_1 \circ h_N$ with values in $W_2$, and let $\mathrm{Sel}_{\mathrm{ev}}$ be the Selmer group of $\rho \circ h_N$ with even values.

An element $\Psi$ of $\mathrm{Sel}_2$ has, for each $j$, an $\epsilon'_j$ component, which is an even cocycle. The cocycle condition for $\rho_1$ couples it to the odd classes through the products $\epsilon_j \epsilon'_j = h$. So a family $(z_j)_{j \le g}$ of even classes *lifts* if some $\Psi \in \mathrm{Sel}_2$ has $\epsilon'_j$ component $z_j$ for every $j$.

The *obstruction bound* $\mathrm{B}_2$ says: there is $C$ such that, for each $m$ and all large $N$, and for every family $z_{i,j}$ ($0 \le i \le g$, $1 \le j \le g$) of elements of $\mathrm{Sel}_{\mathrm{ev}}$ with coefficients in $A_m = A/t^m$, there are $c_0, \dots, c_g \in A$, at least one of them a unit, and $\Psi \in \mathrm{Sel}_2$ whose $\epsilon'_j$ component is $t^C \sum_i c_i z_{i,j}$ for every $j$.

### A counting lemma

**Lemma 7.9.1 (Generator trick).** Let $A$ be a discrete valuation ring with finite residue field $k$ and uniformizer $t$, and let $H$ be a finite $A$-module with $t^m H = 0$. Let $g, C \in \mathbb{N}$ and suppose that $\#(H/t^e H) \le \#k^{ge + C}$ for all $e \le m$. Then for any $\xi_0, \dots, \xi_g \in H$ there are $c_0, \dots, c_g \in A$, one of them a unit, with $t^C \sum_i c_i \xi_i = 0$.

Lean: `UpperTheory.V.Pa.B2.genTrick`.

*Proof.* If $m \le C$ take all $c_i = 1$. Otherwise write $H \cong \bigoplus_s A/t^{a_s}$ with $1 \le a_s \le m$. Then $\#(H/t^e H) = \#k^{\sum_s \min(a_s, e)}$. If $g + 1$ of the $a_s$ exceeded $C$, then $e = C + 1 \le m$ would give $\sum_s \min(a_s, e) \ge (g+1)(C+1) > g(C+1) + C$, against the hypothesis. So $H = H' \oplus H''$, where $t^C H' = 0$ and $H''$ is a quotient of $A^{g}$. Lift the components of the $\xi_i$ in $H''$ to $A^g$. Any $g + 1$ vectors in $A^g$ satisfy a nonzero linear relation over $A$, and after division by a power of $t$ one coefficient is a unit. The relation holds in $H''$, and $t^C$ kills the component in $H'$. $\square$

### The bound from duality

**Theorem 7.9.2 (Obstruction bound from duality).** Let $l \ne 2$. Let $\Gamma$ be a global datum with a Taylor-Wiles datum, $x$ a point of rank $n$ with a basis $\kappa_1, \dots, \kappa_g$ of odd classes, and $\alpha$ a family of eigenvalues. Let $d \in \mathbb{N}$. Suppose that $\Gamma$ satisfies the cohomological axioms for $d$ and some $(d_v)$, and that each $\Gamma_N$ satisfies them for $d$ and some $(d_v)$ that may depend on $N$. Suppose that $\rho$ is trivial on $\Gamma_0 \cap \mathrm{PL}(H)$ and that $\mathrm{Eig}(\alpha)$ holds. Then $\mathrm{B}_2$ holds.

Lean: `UpperTheory.V.Pa.B2.obstructionBound_of_duality`.

*Proof.* Four constants enter, none depending on $m$, $N$ or $e$.

1. By the axioms for $\Gamma$, the odd Selmer group of $\rho$ with coefficients in $A_e$ has at most $\#K^{ge + C_0}$ elements. Here $g$ appears because the $\kappa_j$ generate the odd Selmer group up to a power of $t$.
2. Since $\rho$ is trivial on $\Gamma_0 \cap \mathrm{PL}(H)$ and the eigenvalues at the $\sigma_j$ are distinct, for all large $N$ and all $e \le m$ the odd Selmer group at level $N$ has at most $\#K^{C_n}$ times as many elements as the one at level $\Gamma$.
3. The local invariants $\mathrm{H}^0(G_v, -)$ of the odd part are bounded by $\#K^{C_h}$ for each $v$.
4. The $\varepsilon$-twisted dual invariants of axiom 7 are bounded by $\#K^{C_d}$. This uses that the even matrices are spanned, up to a power of $t$, by the values of $\rho$.

Put $C = C_0 + C_n + C_h \#V + 2 C_d$. Fix $m$ and a large $N$, and let $z_{i,j}$ be given. Let $H$ be the second cohomology of the odd part of the adjoint representation at level $N$ with coefficients in $A_m$, with local conditions, modulo the Selmer second coboundaries. The cocycle condition for a lift is an equation in degree $2$: for each $i$ there is a class $\xi_i \in H$ such that, whenever $\sum_i b_i \xi_i = 0$ in $H$, the family $(\sum_i b_i z_{i,j})_j$ lifts to $\mathrm{Sel}_2$. This uses axiom 6 to lift the unramified conditions at the places $u$.

The group $H$ is finite by the Euler characteristic count, and $t^m H = 0$. For $e \le m$, the exact sequences $0 \to A_{m-e} \to A_m \to A_e \to 0$ and axiom 3 give
$$\#(H/t^e H) \le \#\mathrm{H}^2_{\mathrm{loc}}(A_e) \cdot \#\mathrm{Ck}^2(A_e).$$
The global Euler characteristic formula at level $N$ bounds the first factor by the product of the odd Selmer group (items 1 and 2), the local invariants (item 3) and the dual invariants (item 4). Axiom 7 and item 4 bound the second factor. Together, $\#(H/t^e H) \le \#K^{ge + C}$, and $K$ is the residue field of $A$.

The generator trick now gives $c_0, \dots, c_g$, one of them a unit, with $t^C \sum_i c_i \xi_i = 0$ in $H$. So the family $(t^C \sum_i c_i z_{i,j})_j$ lifts to some $\Psi \in \mathrm{Sel}_2$. $\square$

The only role of $N$ in this proof is through item 2. That is where the Taylor-Wiles places do their work: they make the odd Selmer group at level $N$ no larger, up to a constant, than at the base.

### The arithmetic instance

**Theorem 7.9.3 (Arithmetic obstruction bound).** Assume the published inputs of Galois cohomology. Let $L$ be a CM field with maximal totally real subfield $L^+$, fix a Hida setting with a level $V_0$ whose set of places is that of the setting, a coefficient ring $\mathcal{O}$, a residual datum $r$ of rank $n$, and a Taylor-Wiles datum with Taylor-Wiles places. Assume $\varepsilon \not\equiv 1 \bmod l$ on $\Gamma_0$. Let $x$ be a point with a basis of odd classes, trivial on $\Gamma_0 \cap \mathrm{PL}(H)$, with $\mathrm{Eig}(\alpha)$. Then $\mathrm{B}_2$ holds.

Lean: `UpperTheory.V.Pa.b2Ar`.

*Proof.* The published inputs give the cohomological axioms for the global datum of any level $V$ of the setting, with $d = [L^+ : \mathbb{Q}]$ and $d_v$ the local degrees. Finiteness comes from local and global finiteness, axiom 3 from the global inputs, axioms 4 and 5 from the Euler characteristic formulas, axiom 6 from the tame local computations, and axiom 7 from Poitou-Tate duality. The Taylor-Wiles places identify each $\Gamma_N$, through an injective map of data, with the global datum of a level $V_N$ of the setting, and the axioms transfer along this identification. Apply the obstruction bound from duality with $d = [L^+ : \mathbb{Q}]$. $\square$

The degree $d = [L^+ : \mathbb{Q}]$ is the same here as in the first order bound. In the patching argument this is what makes the numbers of generators and relations of the patched ring match.

**Remark 7.9.4 (Formalization).** The proof of `B2.obstructionBound_of_duality` is in [ObstructionBoundOfDuality.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ArchimedeanH0Cards/ObstructionBoundOfDuality.lean#L145), and the statement `ObstructionBoundFromDuality` is in a file with the other name. The axioms are the structure `CohAx` in [PushforwardPreservesSelmerCocycles.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ArchimedeanH0Cards/PushforwardPreservesSelmerCocycles.lean#L226). The four constants come from `sel0`, `selN`, `H0_local_card_bounded_of_cls_ker_le_ker` and `dualBound`, the classes $\xi_i$ from `transl`, and the size estimate from the private lemma `step`. Our proof of the generator trick follows the structure theorem; we have not checked that the Lean proof of `genTrick` takes the same route. In `b2Ar` ([TaylorWilesObstructionBound.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/AutomorphicDetection/TaylorWilesObstructionBound.lean#L44)) the hypotheses $V_0.S' = s.S$ and $\varepsilon \not\equiv 1 \bmod l$ are both bound to `_` and not used, and the Taylor-Wiles places enter only through the isomorphisms `P.e N` and their injectivity.
