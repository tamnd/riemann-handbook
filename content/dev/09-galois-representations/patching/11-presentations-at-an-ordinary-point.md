---
title: Presentations at an ordinary point
decls:
  - UpperTheory.V.Pa.s6
  - UpperTheory.V.Pa.claim1
  - UpperTheory.V.Pa.pres
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Presentations at an ordinary point

The Selmer bounds of the previous sections live on the Galois side. This section turns them into a statement about rings. We complete the universal ring at the kernel of a point and show two things. The completion carries a representation into an algebra of generalized matrices. Its maximal ideal has a presentation whose number of generators is bounded by the first order Selmer rank. The proof is linear algebra on the tangent space. For the background see [determinants](/learn/deformations-patching/#determinants-and-residually-reducible-representations), [completion](/learn/commutative-algebra/#completion) and [local rings and dimension](/learn/commutative-algebra/#local-rings-and-dimension).

### Ordinary points of the universal ring

Fix a complete discrete valuation ring $\mathcal{O}$ with finite residue field of characteristic $l$, a residual datum $r$ of rank $n$ for a global datum $\Gamma$, and a CO-algebra $B$ over $\mathcal{O}$ with a determinant $D$ of dimension $n$ of $\Gamma_0$ over $B$ compatible with $r$, together with ordinary local characters. Call $(B, D)$ a *pair*. Let $h \colon \Gamma \to \Gamma_{\mathrm{base}}$ be a morphism of global data and $x$ a point of rank $n$ for the base, with ring $A = K[[t]]$.

An *ordinary point at level $h$* consists of: a finite set topologically generating $\Gamma$; an $\mathcal{O}$-algebra map $f \colon B \to A$ under which $D$ and the local characters map to those of $\rho \circ h$; an element $s \in B$ with $f(s) = t$; and auxiliary data $\phi_j, \tau_j$ in $\Gamma_0$ for $j \le q$, with $\phi_j$ and $\tau_j$ commuting, $h(\tau_j) = 1$, and elements $U_{j,i}, y_{j,i}$ of $B$ that kill two families of elements of the group algebra under the trace of $D$. Under $f$, the $y_{j,i}$ go to $0$ and the $U_{j,i}$ go to distinct roots of the characteristic polynomial of $\rho(h(\phi_j))$. The pair values, the $U_{j,i}$, the $y_{j,i}$ and $s$ generate $B$ topologically over $\mathcal{O}$. The *kernel* of the point is the two-sided ideal of the group algebra over $B$ cut out by the Cayley-Hamilton relations of $D$ and by these two families.

Let $\hat B$ be the completion of $B$ at the prime $\ker f$, and let $r_F \colon \hat B \to F$ be the map to the fraction field $F$ of $A$ that extends $f$. Its kernel is the maximal ideal $\mathfrak{m}$ of $\hat B$.

### Generalized matrix algebras

A *generalized matrix representation* over $\hat B$ consists of a finite $\hat B$-algebra $\mathcal{A}$ containing $\hat B$, a complement $N$ of $\hat B$ in $\mathcal{A}$ with $yy' \in \mathfrak{m}$ for all $y, y' \in N$, and a representation $\varrho \colon \Gamma_0 \to M_n(\mathcal{A})$ with:

1. the $\hat B$-span of the values of $\varrho$ is the set of block matrices with entries in $\hat B$ on the two diagonal blocks of sizes $a$ and $n - a$ and entries in $N$ off them;
2. if $a = n$, then $N = 0$;
3. the determinant of $\varrho$ is $D$, and $\varrho(g)^{T}\varrho(cgc) = \varepsilon(g)^{1-n}$;
4. reducing an entry of $\varrho(g)$ modulo $N$ and applying $r_F$ gives the corresponding entry of $\rho(h(g))$;
5. $\varrho$ kills the kernel of the point;
6. for each prime $Q$ of $\hat B$ at which the kernel of the point does not give a semisimple quotient, the annihilator of $N$ lies in $Q$;
7. finiteness and continuity conditions.

Algebras of this kind, with two diagonal blocks and an off-diagonal module, are the generalized matrix algebras of the theory of determinants of Chenevier.

**Theorem 7.11.1 (Generalized matrix algebra at an ordinary point).** Let $l \ne 2$. Let $x$ be a point, $(B, D)$ a pair, $f$ an ordinary point at level $h$, and $\hat B$ a local ring that is the completion of $B$ at $\ker f$. Let $r_F \colon \hat B \to F$ be a ring map with $r_F(b) = f(b)$ for $b \in B$ and with kernel the maximal ideal of $\hat B$. Then a generalized matrix representation over $\hat B$ exists.

Lean: `UpperTheory.V.Pa.s6`.

*Proof.* The completion $\hat B$ is noetherian and complete, and $r_F$ is onto its image field. The element $2$ is a unit in $\hat B$: otherwise $2$ would lie in $\ker r_F$, so $2 = 0$ in $K$, while $2$ is a unit of $\mathbb{Z}_l$ for $l \ne 2$ and maps to a unit of $K$.

Over $\hat B$ the determinant $D$ gives a Cayley-Hamilton algebra $E$ with a trace. Its reduction is the semisimple algebra of $\rho$ over $F$, which is a product of two matrix blocks of sizes $a$ and $n - a$ because $\rho$ is block diagonal and its blocks have the span property. Since $2$ is invertible and $\hat B$ is complete, the block idempotents lift to orthogonal idempotents of $E$ with traces $a$ and $n - a$. The corners of $E$ cut out by these idempotents give the generalized matrix algebra. In type E, with $a < n$, the off-diagonal corners give the module $N$. In type I, with $a = n$, there is one block and $N = 0$. The representation $\varrho$ comes from the action of $\Gamma_0$ on the corners. $\square$

### The tangent space and its cocycles

Fix now, in addition, a complete discrete valuation ring $\mathcal{O}'$ mapping to $\hat B$ such that $\hat B$ is a CO-algebra over $\mathcal{O}'$, the composite $\mathcal{O}' \to \hat B \to F$ is onto, and the images of $A$, of $\mathcal{O}$ and of $s$ in $\hat B$ come from $\mathcal{O}'$. We call all these data a *context*.

Let $I_N \subseteq \hat B$ be the ideal generated by the products $yy'$ with $y, y' \in N$. Put

$$J_2 = \mathfrak{m}_{\mathcal{O}'}\hat B + \mathfrak{m}^2 + I_N,$$

and let $T$ be the $F$-space of additive maps $\alpha \colon \hat B \to F$ with $\alpha(bb') = r_F(b)\alpha(b') + r_F(b')\alpha(b)$ that kill $\mathcal{O}'$ and $I_N$. Each $a \in \mathcal{A}$ is $a = b + y$ with $b \in \hat B$ and $y \in N$. Write $\pi_0(a) = b$. For $\alpha \in T$ put

$$c_\alpha(g) = \bigl(\alpha(\pi_0(\varrho(g)_{ij}))\bigr)_{ij}\, \rho(g)^{-1}.$$

This is the derivative of $\varrho$ along $\alpha$, and it is an even cocycle with bounded denominators. The map $\alpha \mapsto c_\alpha$ is $F$-linear and injective modulo coboundaries.

Over $F$ the three conditions on $A$-cocycles of the previous sections take the following form, with *bounded* meaning that $t^s$ times the cocycle has entries in $A$ for some $s$.

1. *Rank bound $D_0$*: any family of bounded cocycles in $\mathrm{Sel}_1$ with values in $\mathrm{DD}_g(F)$ that is linearly independent modulo $\mathrm{Bd}_1$ has at most $D_0$ elements.
2. *Lifting*: for any $g + 1$ families of $g$ bounded even Selmer cocycles, some nonzero combination lifts to a bounded element of $\mathrm{Sel}_2$.
3. *Spanning*: each bounded odd Selmer cocycle is a combination of the $\kappa_j$ modulo coboundaries.

**Proposition 7.11.2 (Counting lifted tangent directions).** In a context, assume the rank bound $D_0$. Let $\alpha_1, \dots, \alpha_e \in T$ be linearly independent over $F$, and suppose that for all $i$ and $j$ the family with $c_{\alpha_i}$ in place $j$ and $0$ elsewhere lifts to $\mathrm{Sel}_2$. Then $e + g^2 \le D_0$.

Lean: `UpperTheory.V.Pa.claim1`.

*Proof.* Each lift of $c_{\alpha_i}$ gives a bounded $y_i \in \mathrm{Sel}_1$ whose constant part is $c_{\alpha_i}$. For $p, p' \le g$ let $w_{p,p'} = \epsilon_{p'} \kappa_p$. These also lie in $\mathrm{Sel}_1$ and are bounded. We claim that the $e + g^2$ cocycles $y_i$ and $w_{p,p'}$ are independent modulo $\mathrm{Bd}_1$. The rank bound then gives the result.

Suppose $\sum_i c_i y_i + \sum_{p,p'} c_{p,p'} w_{p,p'}$ is the coboundary of an antisymmetric $Y \in W_1$. The constant part of $\rho_1$ is $\rho$, and the $w_{p,p'}$ have constant part $0$. So the constant part gives that $\sum_i c_i c_{\alpha_i}$ is the coboundary of the constant part $Y_0$ of $Y$, an even antisymmetric matrix. Injectivity of $\alpha \mapsto c_\alpha$ modulo coboundaries gives $\sum_i c_i \alpha_i = 0$, so all $c_i = 0$ by independence. Then $Y_0$ is an even antisymmetric invariant of $\rho$, and it is $0$. Next take the $\epsilon_m$ part. Since $Y_0 = 0$, it gives that $\sum_p c_{p,m}\kappa_p$ is the coboundary of the odd matrix $Y_{\epsilon_m}$. The $\kappa_p$ are independent modulo coboundaries, so $c_{p,m} = 0$ for all $p$. $\square$

**Theorem 7.11.3 (Presentation).** In a context, assume the rank bound $D_0$, the lifting condition and the spanning condition. Then there are $X_1, \dots, X_{D_0} \in \mathfrak{m}$, generators $m_1, \dots, m_g$ of $N$ over $\hat B$, and $c_{(i,j),a} \in \mathcal{O}'$ for $i, j \le g$ and $a \le D_0$ such that:

1. the $g^2$ vectors $(\bar c_{(i,j),a})_a$ over the residue field of $\mathcal{O}'$ are linearly independent;
2. $\mathfrak{m} \subseteq (X_1, \dots, X_{D_0}) + J_2$;
3. for each $i$, $\sum_j \bigl(\sum_a c_{(i,j),a} X_a\bigr) m_j \in J_2 N$.

Lean: `UpperTheory.V.Pa.pres`.

*Proof.* We follow five steps.

1. Duality for $T$. The space $T$ is finite dimensional over $F$. An element of $\mathfrak{m}$ killed by every $\alpha \in T$ lies in $J_2$. Every $F$-linear form on $T$ is evaluation at some element of $\mathfrak{m}$.
2. Let $U \subseteq T^g$ be the set of families $(\alpha_j)$ for which $(c_{\alpha_j})_j$ lifts to $\mathrm{Sel}_2$. Lifting is preserved by sums and scalar multiples, and $c$ is linear, so $U$ is a subspace.
3. The lifting condition, applied to $c_\alpha$, shows that any $g + 1$ elements of $T^g$ have a nonzero combination in $U$. So $U$ has codimension at most $g$ in each direction. The counting proposition shows that any independent family $\alpha_1, \dots, \alpha_e$ with every $\alpha_i e_j \in U$ has $e + g^2 \le D_0$.
4. A lemma of linear algebra now gives linear forms $X_1, \dots, X_{D_0}$ on $T$ that span the dual of $T$, and $g^2$ vectors $c$ that are independent over the residue field, such that $\sum_{j,a} c_{(i,j),a} X_a(\alpha_j) = 0$ for each $(\alpha_j) \in U$ and each $i$. Lift the $X_a$ to $\mathfrak{m}$ by step 1 and the coefficients to $\mathcal{O}'$, using that $\mathcal{O}'$ maps onto $F$. Since the $X_a$ span the dual of $T$, step 1 gives item 2.
5. The spanning condition gives generators $m_1, \dots, m_g$ of $N$ whose dual functionals correspond to the $\kappa_j$. Under this correspondence a family in $U$ is exactly a first order direction along which the generators extend. The relations of item 3 then follow from step 4 by a separation argument for functionals on $N/J_2 N$. $\square$

The numbers in the presentation are what the patching argument compares. The maximal ideal needs at most $D_0$ generators over $\mathcal{O}'$ modulo $J_2$, and $g^2$ independent relations tie them to $N$.

**Remark 7.11.4 (Formalization).** The statement `Pres`, the context `Ctx` and the three hypotheses are in [SelmerSpannedByKappaLaurent.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/SelmerScaling/SelmerSpannedByKappaLaurent.lean#L54). The theorem `pres` lives in [AlCSmul.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/SelmerScaling/AlCSmul.lean#L12), and `claim1` in [FirstOrderLiftConstantPart.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/SelmerScaling/FirstOrderLiftConstantPart.lean#L134). Neither file name says what the file proves: the names come from helper lemmas, such as the private `first_order_lift_constant_part` at line 76, which says that the constant part of $\rho_1$ is $\rho$. The private lemma `card_le_of_linearIndependent_mod_bd1_in_sel1` at line 96 of the same file is declared outside the namespace. The generalized matrix representation is the structure `URep` in [PatchedSupportCompletions.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/PatchedSupportCompletions.lean#L78). Its field `ker_le_span_sub_sup_map` at line 98 only says that a certain submodule is finitely generated, so the name does not match the content. Steps 1, 4 and 5 of the presentation are the lemmas `tpDual`, `linAlg`, `dualEx`, `phSep` and `claim2`, which we have not unfolded. The proof of `s6` ([S6.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/AutomorphicDetection/S6.lean#L15)) goes through `hat_ex`, `idem`, `gr_E`, `gr_I` and `urep_of`. Our account of the idempotent lifting follows these names and is not a line by line reading.
