---
title: The statement at one prime
decls:
  - GlobalTheory.ResidueBound.resBound_dsum
  - GlobalTheory.TopBridge.stmtAt_of_real
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The statement at one prime

This section proves the first of the three statements of Section 1, the statement at one prime, for every real local situation. The inputs are local Tate duality, the local Euler characteristic formula and the Bloch-Kato dimension formula, which we state as published theorems, together with the operator $\psi$ of Section 2 and the models of Section 3. The key new step is a bound: classes in $\mathrm{adm}(T_0, \mathcal{O}/\lambda)$ that are independent modulo $\lambda$ number at most $d$. The result is used in [the top theorem](/entry/twisted-lattice-cohomology-theorem-top/).

We first state the published inputs. Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r \ge 1$, and $M$ a finite $\mathbb{Z}/\ell^r$-module with a continuous action of $G_K$ (for the discrete topology on $M$). Put $\mu = \mathbb{Z}/\ell^r(1)$, the group $\mathbb{Z}/\ell^r$ with $G_K$ acting through the cyclotomic character modulo $\ell^r$, and $M^* = \mathrm{Hom}(M, \mu)$.

**Theorem 7.4.1 (Local Tate duality).** $H^2(K, \mu) \cong \mathbb{Z}/\ell^r$, and for $i = 0, 1, 2$ the cup product $H^i(K, M) \times H^{2-i}(K, M^*) \to H^2(K, \mu)$ is a perfect pairing.

This is due to Tate; see Serre, *Galois Cohomology*, Ch. II, §5.2, Theorem 2, and Milne, *Arithmetic Duality Theorems*, Ch. I, Corollary 2.3.

**Theorem 7.4.2 (Local Euler characteristic).** $\#H^1(K, M) = \#H^0(K, M) \cdot \#H^2(K, M) \cdot (\#M)^{[K : \mathbb{Q}_\ell]}$.

See Serre, *Galois Cohomology*, Ch. II, §5.7, Theorem 5, and Milne, *Arithmetic Duality Theorems*, Ch. I, Theorem 2.8.

**Remark 7.4.3.** In the Lean form both theorems are stated for $\mathbb{Z}/\ell^r$-modules with $r \ge 1$, and duality is stated as the bijectivity of the maps from $H^i(K, M)$ to the duals of $H^{2-i}(K, M^*)$ that the cup products induce, in both orders for $i = 1$.

**Theorem 7.4.4 (Bloch-Kato dimension formula).** Let $(K, L)$ be in Case A and $V$ a crystalline representation of $G_K$ over $L$. Then
$$\dim_L H^1_f(K, V) = \dim_L H^0(K, V) + \sum_{\tau} \sum_{a < 0} m_\tau(V, a),$$
where $\tau$ runs over the $\mathbb{Q}_\ell$-embeddings $K \to L$. The double sum is $\dim_L D_{\mathrm{dR}}(V)/\mathrm{Fil}^0$.

See Bloch and Kato, *L-functions and Tamagawa numbers of motives*, in *The Grothendieck Festschrift*, Vol. I, 1990, Corollary 3.8.4.

**Remark 7.4.5.** The Lean form adds two clauses to the formula. For a lattice $T$ of a crystalline $V$, a class $\kappa \in H^1(K, T)$ with $a\kappa \in H^1_f(K, T)$ for some $a \ne 0$ is in $H^1_f(K, T)$. And the finite cocycles of the trivial representation $L$ are the cocycles that vanish on $I_K$. Both follow from the work of Bloch and Kato in the classical setting, but here $H^1_f(K, T)$ is the image of the lattice finite cocycles, so the first clause is a real condition. Below the formula is a hypothesis, asked only in Case A. In the top theorem of Section 5 it is derived from the tie of the period data.

Now fix a local situation and put $\bar k = \mathcal{O}/\lambda$. Let $\bar T = T_0(\chi_1^{-1}) \otimes \bar k$ and $H$, $H_f$ as in Section 1. We say that elements $c_1, \dots, c_s$ of an $\mathcal{O}$-module are *independent modulo $\lambda$* if $\sum_a x_a c_a = 0$ with $x_a \in \mathcal{O}$ implies $\lambda \mid x_a$ for all $a$.

**Definition 7.4.6 (Basic facts on admissible classes).** For a representation $W$ of $G_K$ on an $\mathcal{O}$-module, the *basic facts* hold if for all finite $X$: $\mathrm{adm}(W, X)$ is an $\mathcal{O}$-submodule of $H^1(K, W \otimes X)$; for each $a \ge 1$ with $\lambda^a X = 0$, a class is admissible if and only if it is the class of a cocycle $z$ with $E_a(z)$ admissible, for this $a$; and for each $\mathcal{O}$-linear $f : X \to X'$ to a finite $X'$, the induced map on $H^1$ sends admissible classes to admissible classes, and, if $f$ is injective, a class is admissible when its image is.

**Theorem 7.4.7 (The residual bound).** Assume the conclusion of [the operator $\psi$](/entry/lemma-psi/). Let $S$ be a real local situation for which the basic facts hold for $T_0$. If $c_1, \dots, c_s \in \mathrm{adm}(T_0, \bar k)$ are independent modulo $\lambda$, then $s \le d$.

Lean: `GlobalTheory.ResidueBound.resBound_dsum`.

*Proof.* The ring $\mathcal{O}$ is a discrete valuation ring, finite over $\mathbb{Z}_\ell$, and $\bar k$ is a residue field of the situation. Reality at $\bar k$ gives $R$, a cyclotomic $\iota$, a reduction functor $F$, a model theory $M$ and a map $q : T_0 \to \bar k^r$ as in Section 3. By the basic facts with $a = 1$, each $c_a$ is the class of a cocycle $z_a$ with $E_1(z_a)$ admissible. Through $q$, each $z_a$ becomes a cocycle $z_a' : G_K \to \bar k^r$ for $T$, and $E_1(z_a)$ becomes an extension $E$ of the trivial character by $T$: a representation on $\bar k^{r+1}$ that contains $T$, with a vector $e$ outside $T$ and $g e = e + z_a'(g)$. Since $E_1(z_a)$ is admissible, $E$ has a model. Independence modulo $\lambda$ makes the classes of the $z_a'$ modulo the coboundaries of $T$ linearly independent over $\bar k$. The bound of the model theory then applies. It uses the operator $\psi$ and T1, T2 and T3, and it says that $s$ cocycles of $T$ whose extensions have models and whose classes are independent modulo coboundaries satisfy $s \le d$. $\square$

**Theorem 7.4.8 (Statement at one prime).** Assume local Tate duality and the local Euler characteristic formula for all finite extensions of $\mathbb{Q}_\ell$. Let the period data be tied to a model, with $A_{\inf}$-data. Assume that every local situation is real, and that the Bloch-Kato dimension formula holds for all $(K, L)$ in Case A, with inertia group $I_K$. Then the statement at one prime holds.

Lean: `GlobalTheory.TopBridge.stmtAt_of_real`.

*Proof.* Fix a local situation $S$; the data in the statement at one prime are exactly the data of a local situation. We prove the five parts of the statement.

*Crystalline calculus.* The tie gives the crystalline calculus of Section 3: sums and twists of crystalline lattices are crystalline with the expected jumps, $\varepsilon$ has jump $-1$, and continuous characters trivial on $I_K$ have jump 0.

*Vanishing.* Reality at a finite residue field $k$ gives a model theory with $\omega$ equal to the cyclotomic character modulo $\ell$, and an identification of $\bar T$ with $T$ through $q$. The model theory, with T1, T2 and T3, shows that no subrepresentation of $T$ has a nonzero map to $\omega^{-e}$ for $e = -1, 0$. For $e = 0$ this says $H^0(K, \bar T) = 0$. For $e = -1$ it says that $\bar T$ has no nonzero map to $\mu_\ell$, so $H^0(K, \bar T^*) = 0$, and Tate duality gives $H^2(K, \bar T) = 0$.

*Freeness.* A freeness lemma for the cohomology of a lattice whose reduction modulo $\lambda$ has $H^0 = H^2 = 0$, with the Euler characteristic formula as the count of $H^1$ of finite modules and $n = [K : \mathbb{Q}_\ell]$, shows that $H$ is free of rank $rn$ over $\mathcal{O}$, and that for each finite $X$ the tensor map $H \otimes X \to A(X)$ is injective with the same image as the cocycle map.

*Basic facts.* Admissible modules are closed under submodules, quotients and products. With the crystalline calculus this shows that $T_0 \otimes X$ and $\mathcal{O}(\chi_c) \otimes X$ for $1 \le c \le t$ are admissible for every finite $X$, and then that the basic facts hold for $T_0$.

*The summand.* The Bloch-Kato formula, applied to $V_0(\chi_1^{-1})$, which is crystalline with jumps $u - w_i$ for $u \in U_i$, gives $\dim_L H^1_f = d$: the invariants vanish, and the negative jumps at the letter $i$ are the $d_i$ elements $u < w_i$. Saturation and freeness give a complement of $H_f$ in $H$, and $H_f$ has rank $d$.

*Admissible classes.* The tie gives the extension criterion for crystalline representations, and with the basic facts this shows $H^1_f(X) \subseteq \mathrm{adm}(T_0, X)$ for all finite $X$. [The residual bound](/entry/res-bound-dsum/), with [the operator $\psi$](/entry/lemma-psi/), gives at most $d$ admissible classes independent modulo $\lambda$ at $X = \bar k$. A general lemma on families of submodules $A(X) \subseteq H^1(K, T_0 \otimes X)$ that contain $H^1_f(X)$, are functorial in $X$, reflect along injections, and satisfy this bound, when $H_f$ is a summand of rank $d$, gives $\mathrm{adm}(T_0, X) = H^1_f(X)$. $\square$

**Remark 7.4.9 (Formalization).** The conclusion is called `ErrorExponentStatement`; there is no error exponent in it. Reality is a hypothesis here, and the top theorem supplies it. The vanishing step uses only Tate duality, and the freeness step only the Euler characteristic. The residual bound takes the theorem on $\psi$ as a hypothesis, and the proof of the statement at one prime supplies it.
