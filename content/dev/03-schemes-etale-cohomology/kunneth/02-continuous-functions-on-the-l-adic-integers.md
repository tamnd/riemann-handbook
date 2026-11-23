---
title: Continuous functions on the l-adic integers
decls:
  - GlobalTheory.T.continuous_algebra_universal_property
  - GlobalTheory.CompanionTheory.ContUniv.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Continuous functions on the $\ell$-adic integers

The crystalline comparison of the Galois row uses a site of perfect algebras over the tilt of $\mathcal{O}_{\mathbb{C}_\ell}$. On this site one needs an object that classifies a unit $u$ with $u^\sharp = 1$, the analogue of a point of the multiplicative group that lies over the identity. This section shows that the algebra of continuous functions from $\mathbb{Z}_\ell$ to a perfect algebra $A$ is such an object, with the function $z \mapsto \varepsilon^z$ as the universal unit. The next section uses this universal property to build the line object of the comparison.

**Definition 1.2.1 (Tilt and the element $\varepsilon$).** Let $\ell$ be a prime and $\mathcal{O}^\flat = \varprojlim_{x \mapsto x^\ell} \mathcal{O}_{\mathbb{C}_\ell} / \ell$ the tilt of $\mathcal{O}_{\mathbb{C}_\ell}$. It is a perfect ring of characteristic $\ell$. Let $\ell^\flat \in \mathcal{O}^\flat$ be a compatible system of $\ell$-power roots of $\ell$, let $\xi = \ell - [\ell^\flat]$ in $A_{\inf} = W(\mathcal{O}^\flat)$, and let $\theta : A_{\inf} \to \mathcal{O}_{\mathbb{C}_\ell}$ be Fontaine's map. An *$\varepsilon$-system* is a sequence of units $e_0, e_1, \dots$ of $\mathcal{O}^\flat$ with $e_{m+1}^\ell = e_m$, $\theta([e_0]) = 1$ and $\theta([e_1]) \neq 1$. We write $\varepsilon = e_0$.

For example, a compatible system $(1, \zeta_\ell, \zeta_{\ell^2}, \dots)$ of primitive $\ell$-power roots of unity defines $\varepsilon$ and its roots $e_m$. This is the usual element $\varepsilon$ of [Fontaine's period rings](/learn/galois-representations/#period-rings).

**Definition 1.2.2 (Perfect $\ell$-adic algebra).** A *perfect $\ell$-adic algebra* is a perfect ring $A$ of characteristic $\ell$ with a ring map $s : \mathcal{O}^\flat \to A$ such that $\pi_A = s(\ell^\flat)$ is a nonzerodivisor and $A$ is $\pi_A$-adically complete. A morphism $A \to A'$ is a ring map that commutes with the maps $s$. The ring $\mathcal{O}^\flat$ itself, with $s$ the identity, is the initial object; for each $A$ we write $A^{\mathrm{base}} : \mathcal{O}^\flat \to A$ for the map $s$.

**Definition 1.2.3 (Untilt and sharp map).** For a perfect $\ell$-adic algebra $A$, let $\xi_A$ be the image of $\xi$ in the [[Witt vectors|6N3X2QX4W9]] $W(A)$, and put $U(A) = W(A) / \xi_A$. The *sharp map* is the multiplicative map $a \mapsto a^\sharp$, the image of the Teichmüller lift $[a]$ in $U(A)$. For $A = \mathcal{O}^\flat$ the ring $U(A)$ is $\mathcal{O}_{\mathbb{C}_\ell}$ and $a^\sharp = \theta([a])$.

**Definition 1.2.4 (Test algebra).** A perfect $\ell$-adic algebra $t$ is a *test algebra* if:

1. every monic polynomial of positive degree over $t$ has a root in $t$;
2. for $f, g \in t$ with $\pi_t^N \in (f, g)$ for some $N$, there is an idempotent $e \in t$ with $e f \in (g)$ and $(1 - e) g \in (f)$.

Condition 2 says that, after a decomposition of $\operatorname{Spec} t$ into two clopen pieces, one of $f$ and $g$ divides the other on each piece.

**Definition 1.2.5 (Continuous functions).** Let $A$ be a perfect $\ell$-adic algebra and $\Gamma$ a topological space. Let $C(\Gamma, A)$ be the ring of functions $f : \Gamma \to A$ such that for every $k \geq 0$ the composite $\Gamma \to A \to A / \pi_A^k$ is locally constant. With the constant map $s$, it is a perfect $\ell$-adic algebra. For $\Gamma = \mathbb{Z}_\ell$ we use:

1. the map of constants $c_A : A \to C(\mathbb{Z}_\ell, A)$;
2. the evaluation $\mathrm{ev}_z : C(\mathbb{Z}_\ell, A) \to A$ at $z \in \mathbb{Z}_\ell$;
3. the shift $\sigma(f)(z) = f(z + 1)$;
4. the map $C(\mathbb{Z}_\ell, A) \to C(\mathbb{Z}_\ell, A')$ given by composition with a morphism $A \to A'$;
5. for $m \geq 0$ and $c \in \mathbb{Z}/\ell^m$, the indicator function $\chi_{m,c}$ of the open set $\{z : z \equiv c \bmod \ell^m\}$.

For each $m$, the $\chi_{m,c}$ form a family of [[complete orthogonal idempotents|SS8T32TMEX]], and $\chi_{m,c}$ is the sum of the $\chi_{n,c'}$ with $c' \equiv c \bmod \ell^m$, for $n \geq m$. These are the [[$\ell$-adic integers|V6TJAFZ4MD]] seen through their finite quotients.

**Theorem 1.2.6 (Universal property of continuous functions).** Let $(e_m)$ be an $\varepsilon$-system. There is a unit $\eta$ of $C(\mathbb{Z}_\ell, \mathcal{O}^\flat)$ with:

1. $\eta^\sharp = 1$;
2. $\sigma(\eta) = \varepsilon \cdot \eta$;
3. for all perfect $\ell$-adic algebras $A$, every test algebra $t$, every morphism $\varphi : A \to t$ and every unit $u$ of $t$ with $u^\sharp = 1$, there is a unique morphism $\psi : C(\mathbb{Z}_\ell, A) \to t$ with $\psi \circ c_A = \varphi$ and $\psi(\eta_A) = u$.

Here $\eta_A$ is the image of $\eta$ under composition with $\mathcal{O}^\flat \to A$.

Lean: `GlobalTheory.T.continuous_algebra_universal_property` (also `GlobalTheory.CompanionTheory.ContUniv.main`, the same statement).

The unit $\eta$ is the function $z \mapsto \varepsilon^z$. For $z \in \mathbb{Z}$ this is clear, and the proof extends it to $\mathbb{Z}_\ell$ by continuity. Condition 2 is then $\varepsilon^{z+1} = \varepsilon \cdot \varepsilon^z$. Condition 3 says that maps out of $C(\mathbb{Z}_\ell, A)$ are pairs $(\varphi, u)$: the choice of $u$ is the choice of "which power of $\varepsilon$" the function $\eta$ becomes.

The proof uses two facts about maps out of $C(\mathbb{Z}_\ell, A)$.

**Lemma 1.2.7 (Maps out of continuous functions).** Let $A$ be a perfect $\ell$-adic algebra, $t$ a perfect $\ell$-adic algebra and $\varphi : A \to t$ a morphism. Let $E_m : \mathbb{Z}/\ell^m \to t$ be a family of complete orthogonal idempotents for each $m$, compatible in the sense that $E_m(c) = \sum_{c' \equiv c} E_n(c')$ for $m \leq n$. Then there is a unique morphism $\psi : C(\mathbb{Z}_\ell, A) \to t$ with $\psi \circ c_A = \varphi$ and $\psi(\chi_{m,c}) = E_m(c)$ for all $m$ and $c$.

Lean: `GlobalTheory.CompanionTheory.ContUniv.map_existsUnique`.

*Proof.* For $f \in C(\mathbb{Z}_\ell, A)$ and $m \geq 0$ put $\psi_m(f) = \sum_c E_m(c) \varphi(f(\tilde c))$, where $\tilde c \in \{0, \dots, \ell^m - 1\}$ represents $c$. Since $f$ is locally constant modulo each power of $\pi_A$, the sequence $\psi_m(f)$ is Cauchy for the $\pi_t$-adic topology. Its limit $\psi(f)$ exists because $t$ is complete, and $\psi$ is a morphism with the two properties. A second morphism with the same properties agrees with $\psi$ on each $\psi_m(f)$, hence on the limit. $\square$

**Lemma 1.2.8 (Idempotents from roots of unity).** Let $t$ be a test algebra and $r_0, r_1, \dots \in t$ with $r_{m+1}^\ell = r_m$ and $r_0^\sharp = 1$. For each $m$ there is a family $E_m$ of complete orthogonal idempotents of $t$ indexed by $\mathbb{Z}/\ell^m$ with
$$E_m(c)^\sharp \bigl(r_m^\sharp - (e_m^\sharp)^{c}\bigr) = 0 \quad \text{for all } c.$$

Lean: `GlobalTheory.CompanionTheory.ContUniv.level`.

*Proof.* The element $r_m^\sharp$ of $U(t)$ satisfies $(r_m^\sharp)^{\ell^m} = r_0^\sharp = 1$. The element $e_m^\sharp$ is the image of $\theta([e_m])$, a primitive $\ell^m$-th root of unity. A lemma on test algebras then decomposes $\operatorname{Spec} t$ into clopen pieces on which $r_m^\sharp$ is a fixed power of $e_m^\sharp$. Its idempotents are the $E_m(c)$. $\square$

*Proof of the theorem.*

1. *The unit $\eta$.* A lemma gives $\eta \in C(\mathbb{Z}_\ell, \mathcal{O}^\flat)$ with $\sigma(\eta) = \varepsilon \eta$ and
$$\eta(z) - \varepsilon^{\tilde z_m} \in \pi^{\ell^m} \mathcal{O}^\flat \quad \text{for all } m \text{ and } z,$$
where $\tilde z_m \in \{0, \dots, \ell^m - 1\}$ represents $z \bmod \ell^m$.
2. *Its roots.* The ring $C(\mathbb{Z}_\ell, \mathcal{O}^\flat)$ is perfect, so $\eta$ has a unique compatible system of roots $\rho_m$ with $\rho_0 = \eta$ and $\rho_{m+1}^\ell = \rho_m$. A further lemma computes their sharps:
$$\rho_m^\sharp = \sum_{c \in \mathbb{Z}/\ell^m} \chi_{m,c}^\sharp \, (e_m^\sharp)^{c}.$$
3. *$\eta^\sharp = 1$ and $\eta$ is a unit.* For $m = 0$ the sum has one term, $\chi_{0,0} = 1$, and $e_0^\sharp = 1$, so $\eta^\sharp = 1$. An element whose sharp is a unit is a unit, so $\eta$ is a unit.
4. *Existence of $\psi$.* Given $A$, $t$, $\varphi$ and $u$, let $r_m$ be the roots of $u$ in the perfect ring $t$. The lemma on idempotents from roots of unity gives idempotents $E_m$. Two lemmas on test algebras show that the $E_m$ are compatible: the family at level $n$ sums to a family at level $m$ with the same property, and such a family is unique. The lemma on maps out of continuous functions gives $\psi$ with $\psi \circ c_A = \varphi$ and $\psi(\chi_{m,c}) = E_m(c)$.
5. *$\psi(\eta_A) = u$.* By step 2, $\psi(\rho_m)^\sharp = \sum_c E_m(c)^\sharp (e_m^\sharp)^c$. The relation of the lemma on idempotents makes this equal to $r_m^\sharp$. A compatible system of $\ell$-power roots in $t$ is determined by its sharps, so $\psi(\rho_m) = r_m$ for all $m$, and $\psi(\eta_A) = r_0 = u$.
6. *Uniqueness.* Let $\psi'$ be a second morphism with the two properties. The elements $\psi'(\rho_m)$ are a compatible system of roots of $u$, so they are the $r_m$. The idempotents $\psi'(\chi_{m,c})$ satisfy the relation of the lemma on idempotents by step 2, so they are the $E_m(c)$ by uniqueness. The uniqueness part of the lemma on maps out of continuous functions gives $\psi' = \psi$. $\square$

**Remark 1.2.9.** The statement is the main result of its file, and the theorem `GlobalTheory.T.continuous_algebra_universal_property` passes it on unchanged. The facts used in steps 1, 2 and 4 are statements of other files in the same folder: the existence of the function $z \mapsto \varepsilon^z$, the formula for the sharps of its roots, and two lemmas on coarsening and uniqueness of idempotents. We have read their statements, not their proofs.

**Remark 1.2.10.** The universal property is asserted only for test algebras $t$. The morphism $\psi$ is a limit of finite sums, and the existence of the idempotents $E_m$ needs both conditions of a test algebra. For a general perfect $\ell$-adic algebra $t$ the proof gives nothing, since it needs $r_m^\sharp$ to be locally a power of $e_m^\sharp$.

The theorem is used in [the line object](/entry/line/) of the next section, where it gives the universal property of that object.
